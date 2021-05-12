# Standard Library
import json
import six
import base64
import jwt
import requests
from jwt.algorithms import RSAAlgorithm

# Django
from django.conf import settings
from django.core.cache import cache
from django.utils.functional import cached_property


class TokenError(Exception):
    pass


class TokenValidator:
    def __init__(self, aws_region=None, aws_user_pool=None, audience=None, guest=None):
        self.aws_region = aws_region
        self.aws_user_pool = aws_user_pool
        self.audience = audience
        self.guest = guest

    @cached_property
    def pool_url(self):
        """
        :return: AWS Cognito pool url formatted using local settings
        """

        return 'https://cognito-idp.%s.amazonaws.com/%s' % (self.aws_region, self.aws_user_pool)

    @cached_property
    def _json_web_keys(self):
        response = requests.get(self.pool_url + '/.well-known/jwks.json')
        response.raise_for_status()
        json_data = response.json()
        return {item['kid']: json.dumps(item) for item in json_data['keys']}

    def _get_public_key(self, token=None):
        """
        :param token: AWS Cognito Id/Access token
        :return: token public key after validation with RSAAlgorithm
        Details https://jwt.io/
        """

        try:
            headers = jwt.get_unverified_header(token)
        except jwt.DecodeError as exc:
            raise TokenError(str(exc))

        if getattr(settings, 'COGNITO_PUBLIC_KEYS_CACHING_ENABLED', False):
            cache_key = 'django_cognito_jwt:%s' % headers['kid']
            jwk_data = cache.get(cache_key)

            if not jwk_data:
                jwk_data = self._json_web_keys.get(headers['kid'])
                timeout = getattr(settings, 'COGNITO_PUBLIC_KEYS_CACHING_TIMEOUT', 300)
                cache.set(cache_key, jwk_data, timeout=timeout)
        else:
            jwk_data = self._json_web_keys.get(headers['kid'])

        if jwk_data:
            return RSAAlgorithm.from_jwk(jwk_data)

    def validate(self, token):
        public_key = self._get_public_key(token)

        if not public_key:
            raise TokenError("No key found for this token")

        token_type, payload = self._get_token_type(token)

        # Guest doesn't have audience under 'aud' but under 'client_id'
        audience = self.audience if token_type == 'id' else None

        try:
            jwt_data = jwt.decode(
                token,
                public_key,
                audience=audience,
                issuer=self.pool_url,
                algorithms=['RS256'],
            )
        except (jwt.InvalidTokenError, jwt.DecodeError) as exc:
            raise TokenError(str(exc))

        # Post validate audience for guest
        if token_type == 'access':
            self.validate_access_token_claims(payload)

        return jwt_data

    def validate_access_token_claims(self, token_decoded):
        if self.guest is None and 'client_id' not in token_decoded:
            # Application did not specify an audience, but
            # the token has the 'aud' claim
            raise TokenError('Invalid audience')

        audience_claims = token_decoded['client_id']

        if isinstance(audience_claims, six.string_types):
            audience_claims = [audience_claims]

        if self.guest not in audience_claims:
            raise TokenError('Invalid audience')

    def _get_token_type(self, token):
        """
        Establish token type is ID Token or Access Token.

        :return 'id' or 'access' - based on token_use received from AWS;
                token payload - token payload data decoded using base64 library;
        :rtype str, dict
        """

        token_payload_data = self._decode_token_using_base64(token)

        return token_payload_data.get('token_use', 'id'), token_payload_data

    @staticmethod
    def _decode_token_using_base64(token):
        """
        Decode token using base64 library
        :return Token decoded payload data in case decode process completes successfully
                Emtpy dictionary otherwise
        :rtype dict
        """

        if isinstance(token, six.text_type):
            token = token.encode('utf-8')

        # Decode token using base64
        try:
            signing_value, crypto_segment = token.rsplit(b'.', 1)
            header_segment, claims_segment = signing_value.split(b'.', 1)

            rem = len(claims_segment) % 4

            if rem > 0:
                claims_segment += b'=' * (4 - rem)

            decoded_token = base64.urlsafe_b64decode(claims_segment)
            decoded_token = json.loads(decoded_token)

        except (ValueError, TypeError, AttributeError):
            decoded_token = dict()

        return decoded_token
