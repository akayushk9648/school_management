from django.contrib import admin
from .models import *
# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display=('teacher_id','user','tenant','subject_specialization','hiring_date')
    search_fields=('teacher_id','user','tenant','subject_specialization','hiring_date')
    list_filter=('teacher_id',)
    readonly_fields=('teacher_id',)


admin.site.register(Teacher,TeacherAdmin)
    