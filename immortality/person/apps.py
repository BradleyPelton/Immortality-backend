from django.apps import AppConfig


class PersonConfig(AppConfig):
    name = 'person'  # lowercase person works, uppercase Person does not
