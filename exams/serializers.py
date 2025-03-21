from rest_framework import serializers
from .models import Exam, Result
from classes.models import Class
from students.models import Student
from core.models import Tenant
from classes.models import Subject

class ExamSerializer(serializers.ModelSerializer):
    class_assigned = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all())
    tenant = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())
    
    class Meta:
        model = Exam
        fields = ['exam_id', 'tenant', 'class_assigned', 'exam_name', 'start_date', 'end_date']
        read_only_fields = ['exam_id']

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date must be after start date")
        return data

class ResultSerializer(serializers.ModelSerializer):
    tenant = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    exam = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all())
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    
    class Meta:
        model = Result
        fields = ['result_id', 'tenant', 'student', 'exam', 'subject', 'marks_obtained', 'total_marks']
        read_only_fields = ['result_id']

    def validate(self, data):
    
        if data['marks_obtained'] > data['total_marks']:
            raise serializers.ValidationError("Marks obtained cannot exceed total marks")
        if data['marks_obtained'] < 0:
            raise serializers.ValidationError("Marks obtained cannot be negative")
        if data['total_marks'] <= 0:
            raise serializers.ValidationError("Total marks must be positive")
        return data