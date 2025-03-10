from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import *

class TeacherGetSerializer(serializers.ModelSerializer):
    class Meta:
        models=Teacher
        fields='__all__'
        

class TeacherPostSerializer(serializers.ModelSerializer):
    class Meta:
        models=Teacher
        fields='__all__'


class TeacherPutSerializer(serializers.ModelSerializer):
    class Meta:
        models=Teacher
        fields='__all__'
        