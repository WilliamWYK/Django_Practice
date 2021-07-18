from django.shortcuts import render

# Create your views here.
def menu(request):
    food1 = {
        'name' : '紅燒牛肉麵',
        'price' : 120,
        'comment' : 'good',
        'avalible': True
    }
    food2 = {
        'name' : '清燉牛肉麵',
        'price' : 150,
        'comment' : 'nice',
        'avalible': True
    }
    foods = [food1,food2]
    return render(request,'menu.html',locals())