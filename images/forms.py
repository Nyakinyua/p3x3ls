from django import forms
from .models import *
from pyuploadcare.dj.forms import ImageField




class PostForm(forms.ModelForm):
    '''
    Class that defines how the upload new photo will look like
    '''
    class Meta:
        model = Post
        exclude = ['']
        
