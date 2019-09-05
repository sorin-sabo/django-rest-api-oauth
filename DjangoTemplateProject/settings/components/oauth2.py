import os

# ---------------------------------------------- OAUTH2 CONFIGURATION --------------------------------------------------
# Custom authentication model
AUTH_USER_MODEL = 'api.User'

# Authentication domain based on external service used; e.g. AWS Cognito - user pool; Auth0 - f'https://{AUTH0_DOMAIN}'
AUTH_DOMAIN = os.getenv('AUTH_DOMAIN', None)

# Jwt issuer based on external service used; e.g. AWS Cognito - user pool; Auth0 - f'https://{AUTH0_DOMAIN}'
JWT_ISSUER = os.getenv('JWT_ISSUER', None)

# Jwt guest client id used for extra validation of access token
JWT_CLIENT = os.getenv('JWT_CLIENT', None)
# ---------------------------------------------- END OAUTH2 CONFIGURATION ----------------------------------------------
