# standard library
import json
import jwt
import requests
from jwt.algorithms import RSAAlgorithm
from jwt.exceptions import (
    InvalidAudienceError
)
# noinspection PyPackageRequirements
from jose.jwt import get_unverified_claims

# django
from django.conf import settings
from django.core.cache import cache
from django.utils.functional import cached_property


class TokenError(Exception):
    pass


class TokenValidator:
    """
    Class handles validation for both access and id token.
    """

    def __init__(
            self,
            jwt_auth_domain=getattr(settings, 'AUTH_DOMAIN', None),
            jwt_algorithm=getattr(settings, 'JWT_ALGORITHM', 'RS256'),
            jwt_issuer=getattr(settings, 'JWT_ISSUER', None),
            jwt_client=getattr(settings, 'JWT_CLIENT', None),
            jwt_auth_keyword=getattr(settings, 'JWT_AUTH_FIELD', 'email'),
            ):
        """
        :param str jwt_auth_domain: Authentication domain from external service;
        :param str jwt_algorithm: Algorithm used to decode token by jwt library;
        :param str jwt_issuer: Algorithm used to decode token by jwt library;
        :param str jwt_client: Designates if an extra validation is needed for guest client by providing it's id.
        :param str jwt_auth_keyword: JWT key used to distinguish between logged in user or guest(ID vs ACCESS token)
               Default set to 'email'. Please check https://jwt.io when setting a different value.
        """

        self.jwt_auth_domain = jwt_auth_domain
        self.jwt_algorithm = jwt_algorithm
        self.jwt_issuer = jwt_issuer
        self.jwt_client = jwt_client
        self.jwt_auth_keyword = jwt_auth_keyword

    @cached_property
    def _json_web_keys(self):
        response = requests.get(f'{self.jwt_auth_domain}/.well-known/jwks.json')
        response.raise_for_status()
        json_data = response.json()

        return {item['kid']: json.dumps(item) for item in json_data['keys']}

    def _get_public_key(self, token=None):
        """
        Details https://jwt.io/

        :param token: Id/Access token
        :return: token public key after validation with RSAAlgorithm
        """

        try:
            headers = jwt.get_unverified_header(token)
        except jwt.DecodeError as exc:
            raise TokenError(str(exc))

        if getattr(settings, 'PUBLIC_KEYS_CACHING_ENABLED', False):
            cache_key = 'jwt:%s' % headers['kid']
            jwk_data = cache.get(cache_key)

            if not jwk_data:
                jwk_data = self._json_web_keys.get(headers['kid'])
                timeout = getattr(settings, 'PUBLIC_KEYS_CACHING_TIMEOUT', 300)
                cache.set(cache_key, jwk_data, timeout=timeout)
        else:
            jwk_data = self._json_web_keys.get(headers['kid'])

        if jwk_data:
            return RSAAlgorithm.from_jwk(jwk_data)

    def _validate_access_token_audience(self, jwt_data):
        """
        Extra validation for access token using client id (guest)

        :param jwt_data: Data obtained from token decode;
        :return: None
        """

        if 'sub' not in jwt_data or 'client_id' not in jwt_data:
            return None

        if 'sub' in jwt_data and jwt_data['sub'] != self.jwt_client:
            # Application specified an audience, but it could not be
            # verified since the token does not contain a claim.
            raise InvalidAudienceError('Invalid audience')

        if 'client_id' in jwt_data and jwt_data['client_id'] != self.jwt_client:
            raise InvalidAudienceError('Invalid audience')

    def validate(self, token):
        public_key = self._get_public_key(token)

        if not public_key:
            raise TokenError("No key found for this token")

        unverified_claims = get_unverified_claims(token)

        audience = unverified_claims.get('aud')
        is_guest = unverified_claims.get(self.jwt_auth_keyword) is None

        try:
            jwt_data = jwt.decode(
                token,
                public_key,
                audience=audience,
                issuer=self.jwt_issuer,
                algorithms=[self.jwt_algorithm],
            )
        except (jwt.InvalidTokenError, jwt.ExpiredSignature, jwt.DecodeError) as exc:
            print('Error on decode')
            raise TokenError(str(exc))

        if is_guest and self.jwt_client is not None:
            self._validate_access_token_audience(jwt_data)

        return jwt_data
