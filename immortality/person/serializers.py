from rest_framework import serializers
from person.models import Person


# person Serializer
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
