import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create a superuser if none exists"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username=os.environ.get("DJANGO_SUPERUSER_USERNAME")).exists():
            User.objects.create_superuser(
                username=os.environ.get("DJANGO_SUPERUSER_USERNAME"),
                email=os.environ.get("DJANGO_SUPERUSER_EMAIL"),
                password=os.environ.get("DJANGO_SUPERUSER_PASSWORD"),
            )
            # pylint: disable=no-member
            self.stdout.write(self.style.SUCCESS("Superuser created successfully"))
        else:
            # pylint: disable=no-member
            self.stdout.write(self.style.WARNING("Superuser already exists"))
