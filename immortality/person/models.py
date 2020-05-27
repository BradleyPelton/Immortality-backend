from django.db import models


class Person(models.Model):
    """The model that will hold the information about People stored in the public ledger"""

    """
    TODO- NOTE- BUG MAJOR PROBLEM
    PEOPLE WILL NOT WANT THIS INFORMATION STOLEN BY SCAMMERS
    AN IMPORTANT TRADE OFF, AS MUCH INFO TO IDENTIFY PEOPLE VS MINIMIZE SCAMMERS
    """

    # NAMES
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)

    # BIRTH
    date_of_birth = models.DateTimeField(blank=True, null=True)
    city_of_birth = models.CharField(max_length=100, blank=True)
    country_of_birth = models.CharField(max_length=100, blank=True)

    # NATIONALITY
    # primary_nationality = models.CharField(max_length=100, blank=True)


    # ADMINSTRATIVE 
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)




    # Membership models are generally created with AN INTERMEDIARY MODEL, FamilyRelationship
    # father = models.OneToOneField(
        # 'person.Person',
        # blank=True,
        # through=FamilyRelationshipParticipation
    # )
    # mother = models.OneToOneField('person.Person')

    # age = models.IntegerField()

    def __str__(self):
        return f'<{self.first_name} {self.last_name}>'
