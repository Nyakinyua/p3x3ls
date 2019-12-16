from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image
# Create your views here.

def index(request):
    images = Image.get_images()
    message="This is my message to you"
    return render(request,"index.html", {"message":message,"images":images})

def image(request,id):
    try:
        image = Image.objects.get(id=id)
    except DoesNotExist:
        raise Http404()
    return render(request,'image.html',{'image':image})

def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_images= Image.search_by_category(search_term)
        message = f'{search_term}'
        return render(request,'search.html',{"message":message,"images":searched_images})