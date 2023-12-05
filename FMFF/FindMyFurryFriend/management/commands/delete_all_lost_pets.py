from django.core.management.base import BaseCommand
from FindMyFurryFriend.models import LostPet

class Command(BaseCommand):
    help = 'Deletes all lost pet listings'

    def handle(self, *args, **kwargs):
        LostPet.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All lost pet listings have been deleted.'))
