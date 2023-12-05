from django.db import models
from django.contrib.auth.models import User

class LostPet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    description = models.TextField()
    #image = models.ImageField(upload_to='path/to/upload/directory', blank=True, null=True)


    image = models.ImageField(upload_to='lost_pets/', null=True, blank=True)

    def __str__(self):
        return self.name
class FoundPet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    description = models.TextField()
    #image = models.ImageField(upload_to='path/to/upload/directory', blank=True, null=True)

    image = models.ImageField(upload_to='found_pets/', null=True, blank=True)

    def __str__(self):
        return self.name