from rest_framework import serializers

from .models import Contact, Region, Location, Food, Travel_type, Route, Living

class RegionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
        

class LocationSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'rastoyanie', 'picture', 'regions']
        

class ContactSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'mobile', 'whatsapp', 'telegram', 'created', 'update']
        

class Travel_typeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Travel_type
        fields = '__all__'
        
    
class RouteSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['name', 'rastoyanie', 'travel_type', 'svyzb']
        

class FoodSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['kitchen', 'opisanie' 'price_one_day', 'regions']

        

class LivingSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Living
        fields = ['id', 'name', 'adress', 'card', 'geo_location', 'price', 'location']
        
