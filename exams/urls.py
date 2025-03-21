from django.urls import path
from .views import *
urlpatterns = [
    path('exam/', ExamView.as_view(), name='exam'),
    path('result/', ResultView.as_view(), name='result'),
    ]