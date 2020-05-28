from django.db import models
from immortality.immortality_users.models import ImmortalityUser


class Person(models.Model):
    """The model that will hold the information about People stored in the public ledger"""

    """
    TODO- NOTE- BUG MAJOR PROBLEM
    PEOPLE WILL NOT WANT THIS INFORMATION STOLEN BY SCAMMERS
    AN IMPORTANT TRADE OFF, AS MUCH INFO TO IDENTIFY PEOPLE VS MINIMIZE SCAMMERS
    """

    # NOTE- CHARFIELDS AND TEXTFIELDS SHOULD NEVER HAVE null=True. THEY ARE STORED AS EMPTY STRINGS
    # IN THE DATABASE AND SHOULD NOT BE STORED AS null.

    # ADMINSTRATIVE
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        ImmortalityUser,
        on_delete=models.SET_NULL,
        null=True
    )
    # NAMES
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)

    # BIRTH
    date_of_birth = models.DateTimeField(blank=True, null=True)
    city_of_birth = models.CharField(max_length=100, blank=True)
    country_of_birth = models.CharField(max_length=100, blank=True)

    # DEATH
    date_of_death = models.DateField(blank=True, null=True)
    city_of_death = models.CharField(max_length=100, blank=True)
    country_of_death = models.CharField(max_length=100, blank=True)
    cause_of_death = models.CharField(max_length=100, blank=True)

    # PICTURES- TODO- This is a larger task. I need to set several django settings, including
    # DEFAULT_FILE_STORAGE, STATIC_URL, MEDIA_URL, STATICFILES_DIR
    # profile_picture = models.ImageField()
    # SEE https://docs.djangoproject.com/en/3.0/topics/files/

    # NATIONALITY
    # primary_nationality = models.CharField(max_length=100, blank=True)

    # FAMILY RELATIONSHIPS
    # see https://stackabuse.com/recursive-model-relationships-in-django/
    father = models.ForeignKey(    # Foreign key because ManyToOne is the same as Foreign key
        'self',
        blank=True,    # Blank=True means its not a required field
        null=True,      # null=True sets the value of the column to null in postgres
        on_delete=models.SET_NULL
    )
    mother = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    siblings = models.ManyToManyField(
        'self',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    # age = models.IntegerField()  # Probably easier just to calculate from the frontend

    def __str__(self):
        return f'<Person: {self.first_name} {self.last_name}>'

    def __repr__(self):
        return self.__str__()
