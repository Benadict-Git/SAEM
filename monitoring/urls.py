from django.urls import path
from .views import soil_health

urlpatterns = [
    path('soil-health/', soil_health, name='soil_health'),
]
