from django.test import TestCase
from .models import Location,Category,Image

# Create your tests here.

class LocationTestClass(TestCase):
    # Set up method 
    def setUp(self):
        self.place = Location(name="Yaya")
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance,(self.place,Location))
        
    def test_save_method(self):
        self.place.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)
        
    def test_delete_method(self):
        self.place = Location(name='place')
        self.place.save_location()
        self.place.delete_location()
        location = Location.objects.all()
        self.assertTrue(location)
        
class CategoryTestClass(TestCase):
    def setUp(self):
        
        self.Home = Category(name='Home')

# Testing isinstance
    def test_instance(self):
        self.assertTrue(isinstance(self.Home, Category))

# Testing method
    def test_save_method(self):
        self.Home.save_category()
        category = Category.objects.all()
        self.assertTrue(category)

    def test_delete_method(self):
        self.Home = Category(name='Home')
        self.Home.save_category()
        self.Home.delete_category()
        category = Category.objects.all()
        self.assertTrue(category)
        
class ImagesTestClass(TestCase):
    # setup method
    def setUp(self):

        # creating a new place and saving it
        self.outdoor = Location(name='outdoor')
        self.outdoor.save_place()

        # creating a new order and saving it
        self.new_Home = Category(name='Home')
        self.new_Home.save()

        self.new_image = Image(image_name='Flower', image_description='A hibiscus flower with bee')
        self.new_image.save()

        self.new_images.location.add(self.new_location)
        self.new_images.location.add(self.new_location)

    # Testing isinstance
    def test_instance(self):
        self.assertTrue(isinstance(self.Flower, Image))
        
    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()