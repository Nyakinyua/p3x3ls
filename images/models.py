from django.db import models

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