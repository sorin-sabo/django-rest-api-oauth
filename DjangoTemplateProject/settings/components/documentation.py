# ---------------------------------------------- DRF DOCUMENTATION CONFIGURATION ---------------------------------------
SWAGGER_SETTINGS = {
   'DEFAULT_AUTO_SCHEMA_CLASS': 'apps.api.services.swagger_service.CamelCaseOperationIDAutoSchema',
}

REDOC_SETTINGS = {
    'LAZY_RENDERING': True,
    'HIDE_HOSTNAME': False,
    'PATH_IN_MIDDLE': True,
}
# ---------------------------------------------- END DRF DOCUMENTATION CONFIGURATION -----------------------------------
