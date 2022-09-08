from rest_framework import viewsets
from .models import Contact, Region, Location, Travel_type, Route, Food, Living
from .seriaizers import RegionSerilizer, LocationSerilizer, ContactSerilizer, Travel_typeSerilizer, RouteSerilizer, FoodSerilizer, LivingSerilizer

class RegionViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerilizer


class LocationViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerilizer


class ContactViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerilizer


class FoodViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerilizer


class RouteViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Route.objects.all()
    serializer_class = RouteSerilizer
    
class Travel_typeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Travel_type.objects.all()
    serializer_class = Travel_typeSerilizer


class LivingViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Living.objects.all()
    serializer_class = LivingSerilizer