from django.urls import path
from .views import expenses_dashboard

urlpatterns = [
    path('expenses/', expenses_dashboard, name='expenses_dashboard'),
]
