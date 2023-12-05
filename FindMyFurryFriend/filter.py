import django_filters
from .models import LostPet, FoundPet

class LostPetFilter(django_filters.FilterSet):
    class Meta:
        model = LostPet
        fields = ['species']
        labels = {'species': 'search'}

class FoundPetFilter(django_filters.FilterSet):
    class Meta:
        model = FoundPet
        fields = ['species']
        labels = {'species': 'search'}
