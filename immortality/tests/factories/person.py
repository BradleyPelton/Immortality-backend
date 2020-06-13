import datetime

import factory
import faker

from person.models import Person

fake = faker.Faker()

class PersonFactory(factory.DjangoModelFactory):
    class Meta:
        model = Person

    # id = 
    # created_at = models.DateTimeField(auto_now_add=True)
    # creator = # Needs to be an ImmortalityUser objects
    first_name = fake.first_name()
    # middle_name = models.CharField(max_length=100, blank=True)
    last_name = fake.last_name()

    # BIRTH
    # date_of_birth = models.DateTimeField(blank=True, null=True)
    # city_of_birth = models.CharField(max_length=100, blank=True)
    # country_of_birth = models.CharField(max_length=100, blank=True)

    # # DEATH
    # date_of_death = models.DateField(blank=True, null=True)
    # city_of_death = models.CharField(max_length=100, blank=True)
    # country_of_death = models.CharField(max_length=100, blank=True)
    # cause_of_death = models.CharField(max_length=100, blank=True)

    # FAMILY
    # father =
    # mother =
    # siblings = []

    # OCCUPATION - The primary and secondary occupation someone had in life
    # primary_occupation = models.DateField(blank=True, null=True)
    # secondary_occupation = models.DateField(blank=True, null=True)

    # age = models.IntegerField()  # Probably easier just to calculate from the frontend
