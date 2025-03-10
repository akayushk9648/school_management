from django.urls import path
from .views import *

urlpatterns = [
    path('students/',StudentView.as_view()),
    ] 