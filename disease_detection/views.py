from django.shortcuts import render
from .models import CropImage
from .forms import CropImageForm

def detect_disease(request):
    if request.method == 'POST':
        form = CropImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'disease_detection/result.html', {'message': 'Image uploaded successfully!'})
    else:
        form = CropImageForm()
    
    return render(request, 'disease_detection/upload.html', {'form': form})
