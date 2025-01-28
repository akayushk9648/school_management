from django.db import models
from core.models import Tenant, User
import uuid

class Teacher(models.Model):
    teacher_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='teachers')
    subject_specialization = models.CharField(max_length=255)
    hiring_date = models.DateField()

    def __str__(self):
        return self.user.name
