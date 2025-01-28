from django.contrib import admin
from .models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=('student_id','user','tenant','roll_number','date_of_birth','gender','admission_date','parent_contact')
    search_fields=('student_id','user','tenant','roll_number','date_of_birth','gender','admission_date','parent_contact')
    list_filter=('student_id',)
    readonly_fields=('student_id',)

class AttendanceAdmin(admin.ModelAdmin):
    list_display=('attendance_id','tenant','student','date','status')
    search_fields=('attendance_id','tenant','student','date','status')
    list_filter=('attendance_id',)
    readonly_fields=('attendance_id',)

admin.site.register(Student,StudentAdmin)
admin.site.register(Attendance,AttendanceAdmin)