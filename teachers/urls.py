from django.urls import path
from .views import *

urlpatterns = [
    path('teacher/', TeacherView.as_view()),
    ]