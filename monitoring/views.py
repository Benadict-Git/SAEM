from django.shortcuts import render
from .models import SoilData

def soil_health(request):
    data = SoilData.objects.order_by('-timestamp')[:10]  # Show last 10 entries
    return render(request, 'monitoring/soil_health.html', {'data': data})
