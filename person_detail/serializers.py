from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'age', ]
     #   exclude=['id']
     #   fields='__all__'
        # def validate(self,data):
        #     if data['age']<18:   --> for validation  of age field
        #         raise serializers.ValidationError({'erroe':'age cannot be less than 18'})

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
