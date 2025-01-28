from django.urls import path
from .views import TenantView

urlpatterns = [
    path('tenant/',TenantView.as_view(),name='tenant')
    ]