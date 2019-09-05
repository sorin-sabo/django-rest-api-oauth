# ---------------------------------------------- DEBUG CONFIGURATION ---------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False
# ---------------------------------------------- END DEBUG CONFIGURATION -----------------------------------------------

# ---------------------------------------------- HOST CONFIGURATION ----------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    '.site.com'
]
# ---------------------------------------------- END HOST CONFIGURATION ------------------------------------------------

# ---------------------------------------------- SECURITY CONFIGURATION ------------------------------------------------
# Using a secure-only session cookie makes it more difficult for network traffic sniffers to hijack user sessions.
SESSION_COOKIE_SECURE = True

# Using a secure-only CSRF cookie makes it more difficult for network traffic sniffers to steal the CSRF token.
CSRF_COOKIE_SECURE = True
# ---------------------------------------------- END SECURITY CONFIGURATION --------------------------------------------

# ---------------------------------------------- EMAIL CONFIGURATION ---------------------------------------------------
SERVER_EMAIL = 'noreply@site.com'
# ---------------------------------------------- END EMAIL CONFIGURATION -----------------------------------------------
