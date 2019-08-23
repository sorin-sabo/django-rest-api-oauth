# django
from django.urls import reverse
from django.conf import settings

# rest framework
from rest_framework.test import APITestCase
from rest_framework import status

# local django
from apps.advisor_api.models import AwAdvisor


class AdvisorManagementTests(APITestCase):
    """
    Test CRUD operations for advisors
    ( GET {{apiUrl}}/api/advisor/list/ ) - List
    ( GET {{apiUrl}}/api/advisor/{advisor_id} ) - Read
    ( PUT {{apiUrl}}/api/advisor/{advisor_id} ) - Update
    ( DELETE {{apiUrl}}/api/advisor/{advisor_id} ) - Delete
    ( POST {{apiUrl}}/api/advisor/register/ ) - Create

    @required: settings.FIRM_TOKEN - use a valid firm admin access token
    @required: valid advisor_id on setUp function
    """

    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION=settings.FIRM_TOKEN)
        self.advisor_id = 1

    def tearDown(self):
        self.client.logout()

    def test_advisor_list(self):
        """
        Ensure we can get advisors list for a firm admin.
        """

        url = reverse('advisor_list')

        response = self.client.get(url, format='json')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_401_UNAUTHORIZED])

        if response.status_code != status.HTTP_401_UNAUTHORIZED:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertTrue(isinstance(response.data, list))

            if len(response.data) > 0:
                first_item = response.data[0]
                self.assertTrue('id' in first_item)
                self.assertTrue('external_id' in first_item)
                self.assertTrue('first_name' in first_item)
                self.assertTrue('last_name' in first_item)
                self.assertTrue('email' in first_item)
                self.assertTrue('all_clients_privilege' in first_item)
        else:
            print('UNAUTHORIZED')
    
    def test_advisor_details(self):
        """
        Ensure advisor details are returned correctly.
        """

        url = reverse('advisor_details', kwargs={'advisor_id': self.advisor_id})

        response = self.client.get(url, format='json')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_401_UNAUTHORIZED])

        if response.status_code != status.HTTP_401_UNAUTHORIZED:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertTrue(isinstance(response.data, dict))

            advisor = response.data
            self.assertTrue('id' in advisor)
            self.assertTrue('external_id' in advisor)
            self.assertTrue('first_name' in advisor)
            self.assertTrue('last_name' in advisor)
            self.assertTrue('email' in advisor)
            self.assertTrue('all_clients_privilege' in advisor)
        else:
            print('UNAUTHORIZED')

    def test_advisor_update_with_grant_permission(self):
        """
        Ensure advisor details can be updated.
        Ensure regular advisor can be granted permission to see al company advisors clients.
        """

        url = reverse('advisor_details', kwargs={'advisor_id': self.advisor_id})
        mock_data = {
            "external_id": '2456',
            "all_clients_privilege": True
        }

        response = self.client.put(url, mock_data, format='json')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_401_UNAUTHORIZED])
        updated_advisor = AwAdvisor.objects.get(pk=self.advisor_id)
        permissions = [settings.VIEW_COMPANY_ADVISORS_CLIENTS]

        if response.status_code != status.HTTP_401_UNAUTHORIZED:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            advisor = response.data
            self.assertEqual(mock_data['external_id'], str(advisor['external_id']))
            self.assertEqual(mock_data['all_clients_privilege'], advisor['all_clients_privilege'])

            if hasattr(updated_advisor, 'user') and updated_advisor.user is not None:
                self.assertTrue(updated_advisor.user.has_perms(permissions))
        else:
            print('UNAUTHORIZED')

    def test_advisor_update_with_remove_permission(self):
        """
        Ensure advisor details can be updated.
        Ensure regular advisor permission can be restricted from seeing all company advisors clients.
        """

        url = reverse('advisor_details', kwargs={'advisor_id': self.advisor_id})
        mock_data = {
            'first_name': 'test',
            'last_name': 'another_test',
            'all_clients_privilege': False
        }

        response = self.client.put(url, mock_data, format='json')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_401_UNAUTHORIZED])
        updated_advisor = AwAdvisor.objects.get(pk=self.advisor_id)
        permissions = [settings.VIEW_COMPANY_ADVISORS_CLIENTS]

        if response.status_code != status.HTTP_401_UNAUTHORIZED:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            advisor = response.data
            self.assertEqual(mock_data['first_name'], str(advisor['first_name']))
            self.assertEqual(mock_data['last_name'], str(advisor['last_name']))
            self.assertEqual(mock_data['all_clients_privilege'], advisor['all_clients_privilege'])

            if hasattr(updated_advisor, 'user') and updated_advisor.user is not None:
                self.assertFalse(updated_advisor.user.has_perms(permissions))
        else:
            print('UNAUTHORIZED')

    def test_create_advisor(self):
        """
        Ensure advisor can be created.
        """

        url = reverse('advisor_register')
        mock_data = {
            'first_name': 'test',
            'last_name': 'another_test',
            'email': 'test@test.com',
            'all_clients_privilege': True
        }

        response = self.client.post(url, mock_data, format='json')
        self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_401_UNAUTHORIZED])

        if response.status_code != status.HTTP_401_UNAUTHORIZED:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            advisor = response.data
            self.assertEqual(mock_data['first_name'], str(advisor['first_name']))
            self.assertEqual(mock_data['last_name'], str(advisor['last_name']))
            self.assertEqual(mock_data['all_clients_privilege'], True)
            self.assertEqual(mock_data['email'], advisor['email'])
        else:
            print('UNAUTHORIZED')
