from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import *

class StudentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'


class StudentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields= '__all__'


class StudentPutSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields= '__all__'

class AttendanceGetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields='__all__'

class AttendancePostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields='__all__'
    
    
class AttendancePutSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields='__all__'