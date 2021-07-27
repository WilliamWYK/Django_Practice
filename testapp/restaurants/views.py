from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from restaurants.models import Restaurant, Comment
from django.utils import timezone
from restaurants.form import CommentForm

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
    # error = []
    if request.POST:
        f = CommentForm(request.POST)
        # if any(not request.POST[k] for k in request.POST):
        #     error.append('* 請勿留白')
        if f.is_valid():
            # visitor = request.POST['visitor']
            # content = request.POST['content']
            # email = request.POST['email']
            visitor = f.cleaned_data['visitor']
            content = f.cleaned_data['content']
            email = f.cleaned_data['email']
            date_time = timezone.localtime(timezone.now())
        # if '@' not in email:
        #     error.append('* email格式錯誤')
        # if not error:
        
            Comment.objects.create(
                visitor = visitor,
                content = content,
                email = email,
                date_time = date_time,
                restaurant = restaurant
            )
            f = CommentForm(initial={'content':'請輸入留言.......'})
    else:
        f = CommentForm(initial={'content':'請輸入留言.......'})
    return render(request,'comment.html',locals())

def delete(request):
    if 'rname' in request.GET and request.GET['rname'] != '':
        restaurant = Restaurant.objects.get(name=request.GET['rname'])
    if 'cid' in request.GET and request.GET['cid'] != '':
        Comment.objects.get(id=request.GET['cid']).delete()

    f = CommentForm(initial={'content':'請輸入留言.......'})
    return render(request,'comment.html',locals())