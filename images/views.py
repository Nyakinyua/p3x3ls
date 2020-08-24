from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from .models import *
from django.contrib.auth.decorators import login_required
from . forms import *
from django.contrib.auth import logout
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
    
# @login_required
# def upload_photo(request):
#     title='NewPost'
#     current_user = request.user
#     current_user_id = request.user.id
    
#     if request.method == 'POST':
#         form = UploadPhotoForm(request.post,request.FILES)
#         if form.is_valid():
#             image=form.save(commit=False)
#             image.user=current_user
#             image.userId=current_user_id
#             image.profile=current_user_id
#             image.save()
            
#             return redirect('index')
        
#     else:
#         form = UploadPhotoForm()
#     return render(request,'upload.html',{'title':title,'form':form})

@login_required(login_url='/accounts/login')
def profile(request):
    profile = Profile.objects.filter(user=request.user)
    post = Posts.objects.filter(posted_by=request.user)
    messages = "This is the user profile page"

    return render(request, 'profile.html', {'profile': profile, 'messages': messages, 'post': post})
    
@login_required(login_url="/accounts/login/")
def logout_user(request):
    '''
    view function renders home page once logout
    '''
    
    logout(request)
    return redirect('/')