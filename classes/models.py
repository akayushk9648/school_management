from django.db import models
from core.models import Tenant
from teachers.models import Teacher
import uuid

class Class(models.Model):
    class_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='classes')
    class_name = models.CharField(max_length=100)
    section = models.CharField(max_length=10)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='classes')

    def __str__(self):
        return f"{self.class_name} - {self.section}"


class Subject(models.Model):
    subject_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='subjects')
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='subjects')
    subject_name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='subjects')

    def __str__(self):
        return self.subject_name
