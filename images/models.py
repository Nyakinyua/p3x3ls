from django.db import models
import datetime as dt

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
    
class Image(models.Model):
    image = models.ImageField(upload_to ='images/')
    image_name = models.CharField(max_length=20)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add = True)
    
    def save_image(self):
        return self.save()
    
    def delete_image(self):
        return self.delete()
    
    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images
    
    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(image_id__icontains=id)
        return image
    
    @classmethod
    def filter_by_location(cls,location):
        images = cls.objects.filter(location__image_location__istartswith=location)
        return images
    
    @classmethod
    def filter_by_category(cls, category):
        images = cls.objects.filter(category__image_category__istartswith=category)
        return images
    
    @classmethod
    def search_by_title(cls,search_term):
        image = cls.objects.filter(title__icontains=search_term)
        return image
    
    def 