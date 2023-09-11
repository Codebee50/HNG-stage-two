from django.db import models

# Create your models here.

class Person(models.Model): 
    #the id field will be generated by django 
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name