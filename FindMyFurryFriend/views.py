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
from django.contrib.auth import authenticate
from django.contrib import messages
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

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
def register(request):
    return render(request, 'FindMyFurryFriend/register.html')
def landing(request):
    return render(request, 'FindMyFurryFriend/landing.html')

def base(request):
    return render(request, 'FindMyFurryFriend/base.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('landing')  # Replace 'home' with the actual URL name for your home page
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')

    return render(request, 'FindMyFurryFriend/login.html')
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
        form = LostPetForm(request.POST, request.FILES)
        if form.is_valid():
            lost_pet = form.save(commit=False)

            # Extract latitude and longitude from the POST data with default values
            latitude = request.POST.get('latitude', 0)
            longitude = request.POST.get('longitude', 0)

            # Ensure the values are valid floats; otherwise, use default values
            try:
                lost_pet.latitude = float(latitude)
                lost_pet.longitude = float(longitude)
            except ValueError:
                lost_pet.latitude = 0
                lost_pet.longitude = 0

            lost_pet.save()
            return redirect('lost_pet_detail', pet_id=lost_pet.pk)
    else:
        form = LostPetForm()

    return render(request, 'FindMyFurryFriend/add_lost_pet.html', {'form': form})

def add_found_pet(request):
    if request.method == 'POST':
        form = FoundPetForm(request.POST, request.FILES)
        if form.is_valid():
            found_pet = form.save(commit=False)

            # Extract latitude and longitude from the POST data with default values
            latitude = request.POST.get('latitude', 0)
            longitude = request.POST.get('longitude', 0)

            # Ensure the values are valid floats; otherwise, use default values
            try:
                found_pet.latitude = float(latitude)
                found_pet.longitude = float(longitude)
            except ValueError:
                found_pet.latitude = 0
                found_pet.longitude = 0

            found_pet.save()
            return redirect('found_pet_detail', pet_id=found_pet.pk)
    else:
        form = FoundPetForm()

    return render(request, 'FindMyFurryFriend/add_found_pet.html', {'form': form})


def TN_api(request):
    print("TN_api view called")
    data = {'message': 'Hello, this is Thoa first HTTP API!'}
    return JsonResponse(data)

def post_something(request):
    # Process the post data
    message = "New post available!"

    # Send WebSocket message to the "all_users" group
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)("all_users", {
        "type": "notification.message",
        "message": message,
    })

    return HttpResponse("Post successful")

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