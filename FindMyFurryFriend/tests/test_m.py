from django.test import TestCase
from ..models import LostPet

class LostPetTestCase(TestCase):
    def setUp(self):
        # Create test data
        LostPet.objects.create(name="Test Pet", species="Dog", description="This is a test pet")

    def test_lost_pet_name(self):
        # Get the test pet
        test_pet = LostPet.objects.get(name="Test Pet")

        # Check if the pet's name matches what we created in setUp
        self.assertEqual(test_pet.name, "Test Pet")

    def test_lost_pet_species(self):
        # Get the test pet
        test_pet = LostPet.objects.get(name="Test Pet")

        # Check if the pet's species matches what we created in setUp
        self.assertEqual(test_pet.species, "Dog")

    def test_lost_pet_description(self):
        # Get the test pet
        test_pet = LostPet.objects.get(name="Test Pet")

        # Check if the pet's description matches what we created in setUp
        self.assertEqual(test_pet.description, "This is a test pet")

    def test_lost_pet_creation(self):
        # Create a new LostPet instance
        new_pet = LostPet.objects.create(name="New Pet", species="Cat", description="This is a new pet")

        # Check if the new pet was created successfully
        self.assertIsNotNone(new_pet)
        self.assertEqual(new_pet.name, "New Pet")
        self.assertEqual(new_pet.species, "Cat")
        self.assertEqual(new_pet.description, "This is a new pet")
