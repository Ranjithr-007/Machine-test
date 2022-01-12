from django.db import models
from django.contrib.auth.models import User, auth
from django.db.models.base import Model


class Department(models.Model):
    name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name

class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.BigIntegerField()
    
 
class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name