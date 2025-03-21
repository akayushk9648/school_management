from django.urls import path
from .views import *

urlpatterns = [
        path('class/', ClassView.as_view(), name='class'),
        path('subject/', SubjectView.as_view(), name='subject'),

    ]