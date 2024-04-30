from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Person(models.Model):
    id = models.AutoField(primary_key=True)  
    name=models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)