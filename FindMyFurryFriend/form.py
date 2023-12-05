from django import forms
from .models import LostPet
from .models import FoundPet
class LostPetForm(forms.ModelForm):
    class Meta:
        model = LostPet
        fields = ['species', 'name', 'description', 'image', 'agree_to_share_location', 'latitude', 'longitude']
class FoundPetForm(forms.ModelForm):
    class Meta:
        model = FoundPet
        fields = ['species', 'name', 'description', 'image', 'agree_to_share_location', 'latitude', 'longitude']
