from rest_framework import viewsets
from .models import Contact, Region, Location, Travel_type, Route, Food, Living
from .seriaizers import RegionSerilizer, LocationSerilizer, ContactSerilizer, Travel_typeSerilizer, RouteSerilizer, FoodSerilizer, LivingSerilizer
from accounts.models import User, userProfile

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
    
    def perform_create(self, serializer):
        user = User.objects.get(username=self.request.user)
        userp = userProfile.objects.get(user=user)
        serializer.save(user=userp)

class ContactViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerilizer

    def perform_create(self, serializer):
        user = User.objects.get(username=self.request.user)
        userp = userProfile.objects.get(user=user)
        serializer.save(user=userp)


class FoodViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerilizer


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class RouteViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Route.objects.all()
    serializer_class = RouteSerilizer


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    
class Travel_typeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Travel_type.objects.all()
    serializer_class = Travel_typeSerilizer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)



class LivingViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Living.objects.all()
    serializer_class = LivingSerilizer


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)



