from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from news.models import *
from news.forms import *
from django.contrib.auth.decorators import login_required


# Register your models here.
def index(request):
    blogs = BlogNews.objects.all()
    data = {
        "blogs":blogs,
    }
    return render(request, 'news/index.html', data)

def register(request):
    if request.method  ==  "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
           user = form.save()
           user.save()
           raw_password = form.cleaned_data.get('password1')
           user = authenticate(username=user.username, password=raw_password)
           login(request, user)
           return redirect("/login")    
    else:
        form = SignupForm()
    return render(request, 'news/register.html', {"form":form})

@login_required
def profile(request):
    if request.method  == "POST":
        form = AddNewsForm(request.POST)
        if form.is_valid():
            news_form = form.save(commit=False)
            news_form.user  = request.user
            news_form.save()
            return redirect("allnews")
        
    else:
        form = AddNewsForm()
    return render(request,  'news/profile.html', {"form": form})

def allnews(request):
    mynews = BlogNews.objects.filter(user = request.user)
    data = {
            "mynews": mynews
        }
    return render(request, 'news/allnews.html', data)

def logout(request):
    update = Update.objects.all()
    data = {
            "update": update 
        }
    return render(request, 'news/logout.html', data)

def delete(request, pk):
    item_to_delete = BlogNews.objects.filter (pk=pk).delete()
    
    return redirect(request. META['HTTP_REFERER'])

def thenews(request):
    return render (request, 'news/thenews.html')

def Ebooks(request):
    return render (request, 'news/Ebooks.html')

def form(request):
    if request.method == "POST":
        topic = request.POST.get('topic')
        news = request.POST.get('news')
        blogNews = BlogNews.objects.create( 
            user = request.user,
            topic = topic,
            article = news
        )
    return render (request, 'news/forms.html')


def formation(request):
    if request.method == "POST":
        topic = request.POST.get('topic')
        news = request.POST.get('news')
        complain = Complain.objects.create( 
            topic = topic,
            article = news
        )
    return render (request, 'news/formation.html',)


