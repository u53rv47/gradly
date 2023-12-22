from django.core.management.base import BaseCommand
from core.models import APIKey
import os


class Command(BaseCommand):
    help = "Generates a new API key"

    def handle(self, *args, **kwargs):
        model_name = os.getenv("MODEL_NAME")
        model_id = os.getenv("MODEL_ID")

        if not model_name or not model_id:
            self.stdout.write(
                self.style.WARNING(
                    "Environment variables MODEL_NAME or MODEL_ID are not set."
                )
            )
            return

        api_key = APIKey(model_name=model_name, model_id=model_id)
        api_key.save()

        self.stdout.write(self.style.SUCCESS(f"Generated new API key: {api_key.key}"))
        self.stdout.write(self.style.SUCCESS(f"Model Name: {model_name}"))
        self.stdout.write(self.style.SUCCESS(f"Model ID: {model_id}"))


# python manage.py generateapikey   - command to generate an api key
# Generated new API key: XswU4k7GbephTc0qp8_9MMOJ3CEIiqmYEimXkkuz6s4
# Model Name: gpt-3.5-turbo
# Model ID: gpt-3.5-turbo-16k
