from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image
# Create your views here.

def index(request):
    images = Image.get_images()
    message="This is my message to you"
    return render(request,"index.html", {"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'image.html',{'image':image})