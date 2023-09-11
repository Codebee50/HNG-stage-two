from rest_framework import serializers
from .models import Person
from . import validators

#serializes data according to the Person model, providing a means to validating incoming data
class PersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators = [validators.validate_unique_name])
    class Meta:
        model = Person
        fields= [
            'id',
            'name'
        ]

