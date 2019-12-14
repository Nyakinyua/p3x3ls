from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=45,blank=True)

    def __str__(self):
        return self.name
    
    def save_location(self):
        return self.save()
    
class Category(models.Model):
    name = models.CharField(max_length=45,blank=True)
    
    def save_category(self):
        return self.save()
    
class Image(models.Model):
    image = models.ImageField(Upload_to ='images/')
    image_name = models.CharField(max_length=20)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add = True)