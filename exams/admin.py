from django.contrib import admin
from .models import *


class ExamAdmin(admin.ModelAdmin):
    list_display = ('exam_id', 'tenant', 'class_assigned', 'exam_name', 'start_date', 'end_date')
    search_fields = ('exam_id', 'exam_name')
    list_filter = ('tenant', 'class_assigned', 'start_date', 'end_date')
    readonly_fields = ('exam_id',)
    date_hierarchy = 'start_date'


class ResultAdmin(admin.ModelAdmin):
    list_display = ('result_id', 'tenant', 'student', 'exam', 'subject', 'marks_obtained', 'total_marks')
    search_fields = ('result_id', 'student__user__name', 'exam__exam_name', 'subject__subject_name')
    list_filter = ('tenant', 'exam', 'subject')
    readonly_fields = ('result_id',)
   
   
    def get_percentage(self, obj):
        if obj.total_marks > 0:
            return f"{(obj.marks_obtained / obj.total_marks * 100):.2f}%"
        return "N/A"
    get_percentage.short_description = 'Percentage'


admin.site.register(Exam, ExamAdmin)
admin.site.register(Result, ResultAdmin)