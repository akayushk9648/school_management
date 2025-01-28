from django.contrib import admin
from .models import *
# Register your models here.
class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_id', 'tenant', 'class_name','section','teacher')
    search_fields = ('class_id', 'tenant', 'class_name','section','teacher')
    list_filter = ('class_id',)
    readonly_fields=('class_id',)

class SubjectAdmin(admin.ModelAdmin):
    list_display=('subject_id','tenant','class_assigned','subject_name','teacher')
    search_fields = ('subject_id','tenant','class_assigned','subject_name','teacher')
    list_filter=('subject_id',)
    readonly_fields=('subject_id',)

admin.site.register(Class,ClassAdmin)
admin.site.register(Subject,SubjectAdmin)