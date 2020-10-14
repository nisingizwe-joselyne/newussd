from django.db import models

# Create your models here.
class Farmers(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.firstname
class Harvesting(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    Salary = models.IntegerField()
    location = models.CharField(max_length=45)
    description = models.TextField()
    def __str__(self):
        return self.location
class Registration(models.Model):
    names = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone = models.IntegerField()
   
    def __str__(self):
        return self.names