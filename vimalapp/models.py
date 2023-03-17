
from operator import mod
from re import M
from sre_parse import State
from typing_extensions import Self
from django.db import models
from django.forms import DateField


# Create your models here.
class Contact(models.Model):
    Firstname=models.CharField(max_length=122)
    Lastname=models.CharField(max_length=122)
    Phone=models.CharField(max_length=12)
    Username=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    City = models.CharField(max_length=20)
    date=models.DateField()

    def __str__(self):
        return self.Firstname
    
   
    