from django.db import models
import os

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(null=True, max_length=30)
    last_name = models.CharField(null=True, max_length=30)
    email = models.EmailField(null=True)
    varen_ID = models.IntegerField(null=True, unique=True, default=0)
    keycode = models.IntegerField(null=True, default=0)

    def __str__(self):
        return("{} {}".format(self.first_name, self.last_name))

class Picture(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    picture = models.ImageField(null=True)
    name = models.CharField(null=True, unique=True, max_length=30)
    
    def __str__(self):
        return("{}".format(self.picture.name))
