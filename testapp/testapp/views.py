# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.contrib import auth
from .form import LoginForm
def hello(request,name):
    return HttpResponse('hello {}'.format(name))

def add(request,a,b):
    c = int(a)+int(b)
    return HttpResponse(str(c))

#html要在template裡面作，下面只是測試
def math(request,a,b):
    a = int(a)
    b = int(b)
    plus = a+b
    minus = a-b
    # html = '<html>sum={plus}<br>minus={minus}</html>'.format(plus=plus,minus=minus)
    # return render(request, 'math.html',{'plus':plus,'minus':minus})
    return render(request,'math.html',locals())

def welcome(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('welcome!~'+request.GET['user_name'])
    else:
        return render(request,'welcome.html',locals())

def meta(request):
    values = request.META.items()
    html=[]
    for k,v in values:
        html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k,v))
    return HttpResponse('<table>{}</table>'.format(html))

from restaurants.models import Restaurant
def use_session(request):
    #test for storing obj in session
    r = Restaurant.objects.all()
    request.session['test_obj']= r

    # request.session.set_test_cookie()
    # if request.session.test_cookie_worked():
    #     return HttpResponse('workded')
    # request.session.delete_test_cookie()

    # sid = request.COOKIES['sessionid'] #get session id by cookie
    sid = request.session.session_key #get session id by session
    s = Session.objects.get(pk=sid)

    return HttpResponse(request.session['test_obj'].get(name='GG Paradise').food_set.all()) 

#Custom login from scratch
def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/index/')
    if request.POST:
        f = LoginForm(request.POST)
        if f.is_valid():
            username = f.cleaned_data['username']
            password = f.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/index/')
    else:
        f = LoginForm()
    return render(request,'registration/login.html',locals())

#Custom logout from scratch
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

def home(request):
    cookies = 'no cookies'
    if 'sessionid' in request.COOKIES:
        cookies = request.COOKIES['sessionid']
    is_authenticate = request.user.is_authenticated
    if is_authenticate:
        username = request.user.get_username()
    else:
        username = '遊客'
    return render(request,'index.html',locals())