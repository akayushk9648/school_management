from rest_framework import serializers
from .models import Class, Subject

# Class Serializers
class ClassGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class ClassPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['tenant', 'class_name', 'section', 'teacher']

class ClassPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['class_name', 'section', 'teacher']
        read_only_fields = ['class_id', 'tenant']

# Subject Serializers
class SubjectGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class SubjectPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['tenant', 'class_assigned', 'subject_name', 'teacher']

class SubjectPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['subject_name', 'teacher']
        read_only_fields = ['subject_id', 'tenant', 'class_assigned']