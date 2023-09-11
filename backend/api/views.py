from django.shortcuts import render
from .models import Person
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonSerializer

# Create your views here.

class PersonView(generics.GenericAPIView):

    queryset = Person.objects.all() #the query set that should be used for returning objects from this view
    serializer_class = PersonSerializer #the seializer that should be used for validating and deserializing input
    lookup_field  = 'pk' 

    #used to add a person object
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)#extracting only the data we need from the request body
        serializer.is_valid(raise_exception=True)#throwing an error message if serializer is not valid
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)

    """Retrieves a person object"""
    def get(self, request, *args, **kwargs):
        instance = self.get_object() #uses the look_up field to filter an object from the database 
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

   
    
    #Updates a person object
    def patch(self, request, *args, **kwargs):
        data_serializer = self.get_serializer(data=request.data)
        data_serializer.is_valid(raise_exception=True)

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)

    #deletes a person object 
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'detail': f'{instance.name} deleted succesfully'}, status= status.HTTP_200_OK)

    


