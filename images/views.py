from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.contrib.auth import logout
# Create your views here.

def index(request):
    posts = Post.get_posts()
    message="This is my message to you"
    return render(request,"index.html", {"message":message,"posts":posts})

def image(request,id):
    try:
        image = Post.objects.get(id=id)
    except DoesNotExist:
        raise Http404()
    return render(request,'image.html',{'image':image})

def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_images= Post.search_by_category(search_term)
        message = f'{search_term}'
        return render(request,'search.html',{"message":message,"images":searched_images})
    
def uploadPhoto(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect('/')
    else:
        form = PostForm()
    
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        posts = None
    
    return render(request,'upload.html',{'posts':posts,'form':form})



def profile(request):
    profile = Profile.objects.filter(user=request.user)
    post = Posts.objects.filter(posted_by=request.user)
    messages = "This is the user profile page"

    return render(request, 'profile.html', {'profile': profile, 'messages': messages, 'post': post})
    
