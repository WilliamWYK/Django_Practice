from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from restaurants.models import Restaurant, Comment
from django.utils import timezone

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

def comment(request):
    if 'rname' in request.GET and request.GET['rname'] != '':
        restaurant = Restaurant.objects.get(name=request.GET['rname'])
    else:
        return HttpResponseRedirect('/restaurant_list/')

    if request.POST:
        if len(request.POST['visitor']) > 0 and len(request.POST['content']) > 0:
            visitor = request.POST['visitor']
            content = request.POST['content']
            email = request.POST['email']
            date_time = timezone.localtime(timezone.now())
            Comment.objects.create(
                visitor = visitor,
                content = content,
                email = email,
                date_time = date_time,
                restaurant = restaurant
            )
        else:
            return HttpResponseRedirect('/comment/?rname={}'.format())
    return render(request,'comment.html',locals())