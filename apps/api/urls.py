# django
from django.urls import path

# local django
from apps.api import views


urlpatterns = [
    # USERS
    path(
        route='users/',
        view=views.UserList.as_view(),
        name='system_users'
    ),
]
