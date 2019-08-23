# django
from django.urls import reverse
from django.conf import settings

# rest framework
from rest_framework.test import APITestCase
from rest_framework import status

# local django
from apps.api.models import User


class PermissionsTests(APITestCase):
    """
    Test list operation for user permissions.

    @required: settings.TOKEN - use a valid guest access token /user id token
    """

    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION=getattr(settings, 'TOKEN', ''))
        filters = dict(id=6)  # Change this if you test a specific user
        self.user = User.objects.filter(**filters).first()

    def tearDown(self):
        self.client.logout()

    def test_permissions_list(self):
        """
        Ensure we can get permissions list with details

        - check status code is 200 or 401
        - check response is a list in case of 200
        - check result length is the same with the length of the objects that should be returned
        - check list contains all expected keys (in case is not empty)
        """

        url = reverse('system_permissions')
        response = self.client.get(url, format='json')
        permissions = self.user.get_all_permissions()

        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_401_UNAUTHORIZED])

        if response.status_code != status.HTTP_401_UNAUTHORIZED:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertTrue(isinstance(response.data, list))
            self.assertEqual(len(response.data), len(permissions))

            if len(response.data) > 0:
                first_item = response.data[0]
                self.assertTrue('name' in first_item)
                self.assertTrue('codename' in first_item)
        else:
            print('UNAUTHORIZED')
