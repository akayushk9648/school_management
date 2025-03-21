from django.contrib import admin
from .models import *

# Class Admin Configuration
class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_id', 'tenant', 'class_name', 'section', 'teacher')
    search_fields = ('class_id', 'class_name', 'section')
    list_filter = ('tenant', 'teacher')
    readonly_fields = ('class_id',)

# Subject Admin Configuration
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_id', 'tenant', 'class_assigned', 'subject_name', 'teacher')
    search_fields = ('subject_id', 'subject_name')
    list_filter = ('tenant', 'teacher', 'class_assigned')
    readonly_fields = ('subject_id',)

# Register models with admin site
admin.site.register(Class, ClassAdmin)
admin.site.register(Subject, SubjectAdmin)