from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image
# Create your views here.

def index(request):
    images = Image.get_images()
    message="This is my message to you"
    return render(request,"index.html", {"message":message,"images":images})

def image(request,image_id):
    try:
        images = Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'image.html',{'images':images})

def search_results(request):
    if 'images' in request.GET and request.GET['images']:
        search_term = request.GET.get('images')
        searched_images= Image.search_by_title(search_term)
        message = f'{search_term}'
        return render(request,'search.html',{"message":message,"images":searched_images})