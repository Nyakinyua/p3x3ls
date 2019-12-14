from django.test import TestCase
from .models import Location,Category,Image

# Create your tests here.

class LocationTestClass(Testcase):
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
        
