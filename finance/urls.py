from django.urls import path
from .views import OrganizationView, ReceiptView,Create_ReceiptView, home, invoice


urlpatterns = [
    path('' , home, name='home'),
    path('invoice/' , invoice, name='invoice'),
    path('organization/', OrganizationView.as_view(), name='organization'),
    path('receipt/', ReceiptView.as_view(), name='receipt'),
    path('create_receipt/', Create_ReceiptView.as_view(), name='create_receipt'),
    
]
