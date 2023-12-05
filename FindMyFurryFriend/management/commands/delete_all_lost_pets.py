from django.core.management.base import BaseCommand
from FindMyFurryFriend.models import LostPet
from FindMyFurryFriend.models import FoundPet
class Command(BaseCommand):
    help = 'Deletes all lost and found pet listings'

    def handle(self, *args, **kwargs):
        LostPet.objects.all().delete()
        FoundPet.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All lost and found pet listings have been deleted.'))
