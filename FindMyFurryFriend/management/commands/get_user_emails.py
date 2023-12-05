from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Prints the email addresses of all registered users'

    def handle(self, *args, **options):
        all_users = User.objects.all()

        for user in all_users:
            self.stdout.write(self.style.SUCCESS(user.email))
