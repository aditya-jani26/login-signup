from django.db import models

class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    
class Employees(models.Model):
    
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=500,unique=True)
    address = models.CharField(max_length=500)
    phone = models.IntegerField()

def __str__(self):
    return self.name
