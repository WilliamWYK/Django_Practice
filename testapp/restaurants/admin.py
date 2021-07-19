from django.contrib import admin
from restaurants.models import Restaurant, Food
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number','address')
    search_fields = ('name','phone_number','address')
    ordering = ('name','address')
    fields = ('phone_number','address')

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name','price','comment','is_avalible','restaurant')
    list_filter = ('is_avalible','restaurant')

admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Food,FoodAdmin)