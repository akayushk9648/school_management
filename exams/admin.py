from django.contrib import admin
from .models import *
# Register your models here.

class ExamAdmin(admin.ModelAdmin):
    list_display=('exam_id','tenant','class_assigned','exam_name','start_date','end_date')
    search_fields=('exam_id','tenant','class_assigned','exam_name','start_date','end_date')
    list_filter=('exam_id',)
    readonly_fields=('exam_id',)


class ResultAdmin(admin.ModelAdmin):
    list_display=('result_id','tenant','student','exam','subject','marks_obtained','total_marks')
    search_fields=('result_id','tenant','student','exam','subject','marks_obtained','total_marks')

    list_filter=('result_id',)
    readonly_fields=('result_id',)


admin.site.register(Exam,ExamAdmin)
admin.site.register(Result,ResultAdmin)