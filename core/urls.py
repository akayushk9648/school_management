from django.urls import path
from .views import TenantView,UserView,LogListView

urlpatterns = [
    path('tenant/',TenantView.as_view(),name='tenant'),
    path('user/',UserView.as_view(),name='user'),
    path('log/',LogListView.as_view(),name='log'),
    path('log/<uuid:log_id>/', LogListView.as_view(), name='log-update'),

    ]