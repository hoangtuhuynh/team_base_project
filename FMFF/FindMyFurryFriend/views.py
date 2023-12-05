# FindMyFurryFriend/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import LostPet
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .filter import LostPetFilter
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse
from .form import LostPetForm
from .filter import FoundPetFilter
from .models import FoundPet
from .form import FoundPetForm


def lost_pet_detail(request, pet_id):
    pet = get_object_or_404(LostPet, pk=pet_id)

    # Check if the pet has an image associated with it
    image_url = None  # Initialize image_url to None

    if pet.image:  # Check if the pet has an image
        image_url = pet.image.url

    return render(request, 'FindMyFurryFriend/lost_pet_detail.html', {'pet': pet, 'image_url': image_url})

def found_pet_detail(request, pet_id):
    pet = get_object_or_404(FoundPet, pk=pet_id)

    # Check if the pet has an image associated with it
    image_url = None  # Initialize image_url to None

    if pet.image:  # Check if the pet has an image
        image_url = pet.image.url

    return render(request, 'FindMyFurryFriend/found_pet_detail.html', {'pet': pet, 'image_url': image_url})
def landing(request):
    return render(request, 'FindMyFurryFriend/landing.html')

def lost_pet_list(request):
    # Create a filter instance and apply it to the queryset
    lost_pet_filter = LostPetFilter(request.GET, queryset=LostPet.objects.all())

    # Check if the form has been submitted and if it is valid
    if request.method == 'GET' and lost_pet_filter.is_valid():
        # Apply the filter to the queryset
        lost_pets = lost_pet_filter.qs
    else:
        # If the form is not submitted or is not valid, display all lost pets
        lost_pets = LostPet.objects.all()

    return render(request, 'FindMyFurryFriend/lost_pet_list.html', {'lost_pets': lost_pets, 'filter': lost_pet_filter})

def found_pet_list(request):
    # Create a filter instance and apply it to the queryset
    found_pet_filter = FoundPetFilter(request.GET, queryset=FoundPet.objects.all())

    # Check if the form has been submitted and if it is valid
    if request.method == 'GET' and found_pet_filter.is_valid():
        # Apply the filter to the queryset
        found_pets = found_pet_filter.qs
    else:
        # If the form is not submitted or is not valid, display all found pets
        found_pets = FoundPet.objects.all()

    return render(request, 'FindMyFurryFriend/found_pet_list.html', {'found_pets': found_pets, 'filter': found_pet_filter})


def add_lost_pet(request):
    if request.method == 'POST':        
        if request.user.is_authenticated:
            owner = request.user
        else:
            owner = None
            
        form = LostPetForm(request.POST, request.FILES)  # Handle files with request.FILES

        if form.is_valid():
            new_lost_pet = form.save()
            return redirect('lost_pet_list')
        else:
            # Handle form validation errors here (e.g., display an error message)
            pass
    else:
        form = LostPetForm()
    return render(request, 'FindMyFurryFriend/add_lost_pet.html', {'form': form})

def add_found_pet(request):
    if request.method == 'POST':        
        if request.user.is_authenticated:
            owner = request.user
        else:
            owner = None
            
        form = FoundPetForm(request.POST, request.FILES)  # Handle files with request.FILES

        if form.is_valid():
            new_found_pet = form.save()
            return redirect('found_pet_list')
        else:
            # Handle form validation errors here (e.g., display an error message)
            pass
    else:
        form = FoundPetForm()
    return render(request, 'FindMyFurryFriend/add_found_pet.html', {'form': form})


def TN_api(request):
    print("TN_api view called")
    data = {'message': 'Hello, this is Thoa first HTTP API!'}
    return JsonResponse(data)

class LostPetListViewTest(TestCase):
    def test_lost_pet_list(self):
        # Create a sample LostPet object for testing
        LostPet.objects.create(name="Test Pet", species="Dog", description="Test Description")

        # Access the view using a test client
        response = self.client.get(reverse('lost_pet_list'))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the sample pet's name
        self.assertContains(response, "Test Pet")



