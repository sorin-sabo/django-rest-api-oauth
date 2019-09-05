# ---------------------------------------------- REST FRAMEWORK CONFIGURATION ------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'apps.api.permissions.CustomDjangoModelPermission',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'apps.oauth2.TokenAuthentication'
    ],
}
# ----------------------------------------------- END REST FRAMEWORK CONFIGURATION -------------------------------------
