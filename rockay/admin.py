
from django.contrib import admin
from .models import Region, Location, Food, Travel_type, Route, Living, Contact
# Register your models here.
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'rastoyanie', 'picture', 'regions']
    list_filter = ['regions']
    search_fields = ['name', 'picture', 'regions']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile', 'telegram', 'whatsapp', 'home', 'user', 'created', 'update']
    search_fields = ['name', 'home', 'email']

class FoodAdmin(admin.ModelAdmin):
    list_display = ['kitchen', 'opisanie', 'price_one_day', 'regions']
    list_filter = ['regions']
    search_fields = ['price_one_day']
    

class Travel_typeAdmin(admin.ModelAdmin):
    list_display = ['name', 'mesto', 'price_one_mesto']
    search_fields = ['name', 'mesto']

class RouteAdmin(admin.ModelAdmin):
    list_display = ['name', 'rastoyanie', 'travel_type', 'svyzb']
    list_filter = ['travel_type', 'svyzb']
    search_fields = ['name','travel_type']

class LivingAdmin(admin.ModelAdmin):
    list_display = ['name', 'adress', 'card', 'price', 'geo_location', 'location']
    list_filter = ['location']
    search_fields = ['name', 'adress', 'price']


admin.site.register(Region, RegionAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Travel_type, Travel_typeAdmin)
admin.site.register(Living, LivingAdmin)
admin.site.register(Contact, ContactAdmin)