from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Person
from .serializers import PersonSerializer

import django_filters



# class PersonFilter(django_filters.rest_framework.FilterSet):
#     """ CREATE A CUSTOM FILTER???? """
# see
# https://www.django-rest-framework.org/api-guide/filtering/
# https://django-filter.readthedocs.io/en/stable/guide/usage.html

#     def __init__(self, request):
#         # FILTER BACKEND????
#         first_name = django_filters.CharFilter(
#             field_name=first_name
#         )

#         class meta():
#             model = Person
#             fields = ['first_name', 'last_name', ]

class PersonList(APIView):
    """
    List all people, or create a new Person.
    """
    # filterset_class = PersonFilter

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """

        # EXAMPLE REQUEST
        # http://localhost:8000/api/person/?first_name=Thomas&last_name=Anderson

        queryset = Person.objects.all()
        r_first_name = self.request.query_params.get('first_name', None)
        r_last_name = self.request.query_params.get('last_name', None)
        # r_username = self.request.query_params.get('date_of_birth', None)
        # r_birth_country = self.request.query_params.get('birth_country', None)
        # r_birth_year = self.request.query_params.get('birth_country', None)
        # r_birth_date = self.request.query_params.get('birth_country', None)
        if r_first_name is not None:
            queryset = queryset.filter(first_name__iexact=r_first_name)
        if r_last_name is not None:
            queryset = queryset.filter(last_name__iexact=r_last_name)
        # if r_birth_country is not None:
        #     queryset = queryset.filter(birth_country__iexact=r_birth_country)
        # if r_birth_year is not None:
        #     queryset = queryset.filter(birth_country__iexact=r_birth_country)
        # if r_birth_country is not None:
        #     queryset = queryset.filter(birth_country__iexact=r_birth_country)
        return queryset

    def get(self, request, format=None):
        people = self.get_queryset()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Create a new Person object."""
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonDetail(APIView):
    """
    Retrieve, update or delete a Person instance.
    """
    def get_object(self, id):
        try:
            return Person.objects.get(id=id)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        person = self.get_object(id)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        person = self.get_object(id)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        person = self.get_object(id)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






# rm db.sqlite3
# winpty python manage.py makemigrations
# winpty python manage.py migrate --run-syncdb

# winpty python manage.py shell_plus

# Person.objects.create(first_name='Thomas', last_name='Anderson')
# Person.objects.create(first_name='Trinity', last_name='Anderson')
# Person.objects.create(first_name='Morpheus', last_name='Daniel')
# Person.objects.create(first_name='Agent', last_name='Smith')
# Person.objects.create(first_name='Merovingian', last_name='Frenchman')
# Person.objects.create(first_name='Key', last_name='Maker')
