"""
DjangoTemplateProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# django
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

# documentation library
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# third party app for 2 factor auth
from django_otp.admin import OTPAdminSite

# local api
from apps.api.permissions.custom_permissions import CanSeeApiDocs
from rest_framework.authentication import SessionAuthentication


admin.site.site_header = "API administration"
admin.site.site_title = "API administration"
admin.site.index_title = "Template API Administration"
admin.site.site_url = "/docs"
admin.site.__class__ = OTPAdminSite

schema_view = get_schema_view(
    openapi.Info(
        title="Django Template API",
        default_version='v1.0',
        description="Django 2.2.4 api",
        contact=openapi.Contact(email="sabo.sorin@ymail.com"),
    ),
    validators=['flex'],
    public=True,
    permission_classes=(CanSeeApiDocs, ),
    authentication_classes=(SessionAuthentication,)
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # API DOCUMENTATION
    path(
        route='docs/',
        view=login_required(schema_view.with_ui('redoc', cache_timeout=0)),
        name='schema_redoc'
    ),

    # CONFIGURATION API
    path(
        route='api/system/',
        view=include('apps.api.urls'),
        name='system_api'
    ),

    # CRUD API
    path(
        route='api/product/',
        view=include('apps.crud_api.urls'),
        name='crud_api'
    ),
]
