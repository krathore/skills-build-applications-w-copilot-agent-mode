from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from octofit_tracker.models.user import UserProfile

class UserProfileAPITestCase(APITestCase):
    def setUp(self):
        self.user = UserProfile.objects.create(username='testuser', email='test@example.com')

    def test_list_users(self):
        url = reverse('userprofile-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
