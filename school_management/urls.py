from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/finance/', include('finance.urls')),
    path('api/students/', include('students.urls')),
    path('api/teachers/', include('teachers.urls')),
    path('api/core/', include('core.urls')),
    path('api/exams/', include('exams.urls')),
    path('api/classes/', include('classes.urls')),
]
