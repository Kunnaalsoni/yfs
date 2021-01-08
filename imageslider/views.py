from django.shortcuts import render
from .models import imageslider
# Create your views here.
def homePage(request):
    image = imageslider.objects.all()
    return render(request, 'index.html', {'image': image})
