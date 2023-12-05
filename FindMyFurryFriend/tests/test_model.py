from django.test import TestCase
from django.contrib.auth.models import User
from ..models import LostPet

class LostPetModelTest(TestCase):

    def test_lost_pet_str_representation(self):
        # Create a User instance
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a LostPet instance
        lost_pet = LostPet.objects.create(owner=user, name='Fluffy', species='Dog', description='A cute dog')

        # Check if the __str__ method returns the expected string representation
        self.assertEqual(str(lost_pet), 'Fluffy')

    def test_lost_pet_with_image(self):
        # Create a User instance
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a LostPet instance with an image (replace 'path_to_test_image.jpg' with the actual path)
        lost_pet = LostPet.objects.create(owner=user, name='Rover', species='Dog', description='Another dog')
        with open('path_to_test_image.jpg', 'rb') as image_file:
            lost_pet.image.save('test_image.jpg', image_file)

        # Retrieve the created LostPet instance
        pet_with_image = LostPet.objects.get(name='Rover')

        # Check if the image field is not None
        self.assertIsNotNone(pet_with_image.image)
