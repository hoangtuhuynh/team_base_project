from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import LostPet

class LostPetViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_lost_pet_list_view(self):
        # Verify that the view returns a status code of 200 for a valid GET request.
        response = self.client.get(reverse('FindMyFurryFriend:lost_pet_list'))
        self.assertEqual(response.status_code, 200)

    def test_add_lost_pet_view(self):
        # Test that the view redirects to the `lost_pet_list` URL after successfully adding a lost pet.
        response = self.client.post(reverse('FindMyFurryFriend:add_lost_pet'), {'name': 'Fluffy', 'species': 'Dog', 'description': 'A cute dog'})
        self.assertRedirects(response, reverse('FindMyFurryFriend:lost_pet_list'))

        # Test that the view handles a POST request with invalid data correctly.
        response = self.client.post(reverse('FindMyFurryFriend:add_lost_pet'), {'name': '', 'species': 'Dog', 'description': 'A cute dog'})
        self.assertEqual(response.status_code, 200)  # Expecting a re-render of the form due to validation error

        # Test that the view handles a GET request correctly.
        response = self.client.get(reverse('FindMyFurryFriend:add_lost_pet'))
        self.assertEqual(response.status_code, 200)

    def test_lost_pet_detail_view(self):
        # LostPet instance for testing
        lost_pet = LostPet.objects.create(name='Fluffy', species='Cat', description='A cute cat')

        # Test that the view returns a status code of 200 for a valid pet ID.
        response = self.client.get(reverse('FindMyFurryFriend:lost_pet_detail', args=[lost_pet.id]))
        self.assertEqual(response.status_code, 200)

        # Test that the view returns a 404 status code for an invalid pet ID.
        response = self.client.get(reverse('FindMyFurryFriend:lost_pet_detail', args=[1000]))  # Assuming 1000 is an invalid ID
        self.assertEqual(response.status_code, 404)
