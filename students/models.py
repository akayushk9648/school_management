from django.db import models
from core.models import Tenant, User
from classes.models import Class
import uuid
class Student(models.Model):
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='students')
    roll_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    admission_date = models.DateField()
    parent_contact = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.name} ({self.roll_number})"


class Attendance(models.Model):
    attendance_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='attendance')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student.user.name} - {self.date}"
