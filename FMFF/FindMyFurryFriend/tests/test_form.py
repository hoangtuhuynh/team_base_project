from django.test import TestCase
from .models import LostPet
from .forms import LostPetForm

class LostPetFormTestCase(TestCase):
    def test_lost_pet_form_valid(self):
        # Create a dictionary with form data
        form_data = {
            'name': 'Elmo',
            'species': 'Dog',
            'description': 'Elmo likes cookies.',
            'image': None  # Assuming image is optional (nullable and blank)
        }

        # Create a form instance with the data
        form = LostPetForm(data=form_data)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_lost_pet_form_invalid(self):
        # Create a dictionary with invalid form data (e.g., missing required fields)
        form_data = {
            'name': '',  # Missing required field
            'species': 'Cat',
            'description': 'Garfield loves lasagna.',
            'image': None  # Assuming image is optional (nullable and blank)
        }

        # Create a form instance with the invalid data
        form = LostPetForm(data=form_data)

        # Check if the form is not valid
        self.assertFalse(form.is_valid())

    def test_lost_pet_form_blank_image_valid(self):
        # Create a dictionary with form data, including a blank (None) image
        form_data = {
            'name': 'Garfield',
            'species': 'Cat',
            'description': 'Garfield loves lasagna.',
            'image': None
        }

        # Create a form instance with the data
        form = LostPetForm(data=form_data)

        # Check if the form is valid
        self.assertTrue(form.is_valid())
