from rest_framework import serializers
from .models import Employee, Picture

# Serializer for the Employee class
class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("first_name", "last_name", "email", "varen_ID", "keycode")

# Serializer for the Picture class
class PicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ("employee", "picture", "name")