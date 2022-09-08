from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=25)
    rastoyanie = models.CharField(max_length=100000)
    picture = models.ImageField(upload_to='last_praject/bye/static/')
    is_active = models.BooleanField(default=False)
    regions = models.ForeignKey(Region, verbose_name='region', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=100)
    home = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Travel_type(models.Model):
    name = models.CharField(max_length=25)
    mesto = models.IntegerField()
    price_one_mesto = models.IntegerField()
    

    def __str__(self):
        return self.name

class Route(models.Model):
    name = models.CharField(max_length=25)
    rastoyanie = models.CharField(max_length=100000)
    is_active = models.BooleanField(default=False)
    travel_type = models.ForeignKey(Travel_type, verbose_name='traveltype', on_delete=models.CASCADE)
    svyzb = models.ForeignKey(Location, verbose_name='travelvid', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Food(models.Model):
    kitchen = models.CharField(max_length=500)
    opisanie = models.CharField(max_length=1000)
    price_one_day = models.IntegerField()
    is_active = models.BooleanField(default=False)
    regions = models.ForeignKey(Location, verbose_name='region', on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Living(models.Model):
    name = models.CharField(max_length=25)
    adress = models.CharField(max_length=60)
    card = models.ImageField(upload_to='static/')
    geo_location = models.IntegerField()
    price = models.TextField()
    is_active = models.BooleanField(default=False)
    location = models.ForeignKey(Location, verbose_name='region', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

