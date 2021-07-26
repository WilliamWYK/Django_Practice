# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

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
