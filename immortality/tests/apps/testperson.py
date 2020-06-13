import pytest

from django.db import IntegrityError
from django.test import TestCase

from person.models import Person
from tests.factories.person import PersonFactory


# @pytest.mark.django_db
class PersonTests(TestCase):
    
    def test_duplicate_first_and_last_names(self):
        """test creating two users with identical first and last names"""

        bob_one = PersonFactory(first_name='Bob', last_name='Anderson')
        bob_two = PersonFactory(first_name='Bob', last_name='Anderson')

        all_bobs_query = Person.objects.filter(first_name='Bob', last_name='Anderson')

        print("asserting Persontest")
        self.assertLess(len(all_bobs_query), 1)
        # assert len(all_bobs_query) > 1, "failed to find more than one Bob Anderson"
