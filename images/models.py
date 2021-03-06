from django.db import models
import datetime as dt
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    name = models.TextField(max_length=45,blank=True)

    def __str__(self):
        return self.name
    
    def save_location(self):
        return self.save()
    
    def delete_location(self):
        return self.delete()
    
class Category(models.Model):
    name = models.TextField(max_length=45,blank=True)
    
    def save_category(self):
        return self.save()
    
    def delete_category(self):
        return self.delete()
    
    def __str__(self):
        return self.name
    
# class Image(models.Model):
#     joy_image = ImageField(blank=True,manual_crop="")
#     image_name = models.CharField(max_length=20)
#     description = models.TextField()
#     location = models.ForeignKey(Location,on_delete=models.CASCADE)
#     category = models.ForeignKey(Category,on_delete=models.CASCADE)
#     pub_date = models.DateTimeField(auto_now_add = True)
    
#     def __str__(self):
#         return self.image_name
    
#     def save_image(self):
#         return self.save()
    
#     def delete_image(self):
#         return self.delete()
    
#     @classmethod
#     def get_images(cls):
#         images = cls.objects.all()
#         return images
  
    
#     @classmethod
#     def filter_by_location(cls,location):
#         images = cls.objects.filter(location__image_location__istartswith=location)
#         return images
    
#     @classmethod
#     def filter_by_category(cls, category):
#         images = cls.objects.filter(category__image_category__istartswith=category)
#         return images
    
#     @classmethod
#     def search_by_category(cls,search_term):
#         image = cls.objects.filter(category__name__icontains=search_term)
#         return image
    
#     @classmethod
#     def search_users(cls,term):
#         result=cls.objects.filter(user__username__icontains=term)
#         return user
    
    
#     class Meta:
#         ordering =  ['image_name']
        
class Profile(models.Model):
    '''
    Class that creates instance of a new user
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000)
    profile_photo = ImageField(blank=True,manual_crop="")
    
    
    def __str__(self):
        return self.bio
    
    def save_profile(self):
        return self.save()
    
    def delete_profile(self):
        profile=Profile.objects.all().delete()
        return profile

class Post(models.Model):
    photo = ImageField(blank=True, manual_crop="")
    image_name = models.CharField(max_length=20,default='img')
    description = models.TextField(default='Basic Desc')
    location = models.ForeignKey(Location,on_delete=models.CASCADE,default='curr Loc')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default='Photos')
    pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.image_name
    
    def save_image(self):
        return self.save()
    
    def delete_image(self):
        return self.delete()

    @classmethod
    def get_posts(cls):
        posts = cls.objects.all()
        return posts

    @classmethod
    def filter_by_location(cls,location):
        posts  = cls.objects.filter(location__image_location__istartswith=location)
        return posts 
    
    @classmethod
    def filter_by_category(cls, category):
        posts  = cls.objects.filter(category__image_category__istartswith=category)
        return posts 
    
    @classmethod
    def search_by_category(cls,search_term):
        posts  = cls.objects.filter(category__name__icontains=search_term)
        return posts 
    
    @classmethod
    def search_users(cls,term):
        result=cls.objects.filter(user__username__icontains=term)
        return user
    
    
    class Meta:
        ordering =  ['pub_date']