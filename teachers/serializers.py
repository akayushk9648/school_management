from rest_framework import serializers
from .models import *

class TeacherGetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields='__all__'
        

class TeacherPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=['user','tenant','subject_specialization','hiring_date']


class TeacherPutSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields = ['subject_specialization', 'hiring_date']
        read_only_fields = ['teacher_id', 'user', 'tenant']
        