from django.db import models
from django.conf import settings
from django.db.models.fields import DateField


class Contact(models.Model):
    author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    prename =  models.CharField(max_length=50, default=None)
    lastname =  models.CharField(max_length=50, default=None)
    email = models.CharField(max_length=50, default=None)
    phonenumber = models.CharField(max_length=50, default=None)
    color = models.CharField(max_length=20, default=None)

class Todo(models.Model):
    author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    created_at = models.CharField(max_length=20, default=None)
    expire_date = models.CharField(max_length=20, default=None, null=True)
    description = models.TextField(max_length=500, default=None)
    name = models.CharField(max_length=50, default=None)
    category = models.CharField(max_length=20, default=None)
    priority = models.CharField(max_length=20, default=None)
    development_state = models.CharField(max_length=20, default=None)
    contacts = models.ManyToManyField(Contact)

   
    

