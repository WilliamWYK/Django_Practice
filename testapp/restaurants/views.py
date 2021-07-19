from django.shortcuts import render
from django.http import HttpResponseRedirect
from restaurants.models import Restaurant, Food

# Create your views here.
def menu(request):
    if 'rname' in request.GET and request.GET['rname'] != '':
        restaurant = Restaurant.objects.get(name=request.GET['rname'])
        return render(request,'menu.html',locals())
    else:
        return HttpResponseRedirect('/restaurant_list/')
    # path = request.META.items()
    # path = request.get_full_path()
    #path = request.path
    # path = request.is_secure()
    # path = request.get_host()
    

def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request,'restaurant_list.html',locals())