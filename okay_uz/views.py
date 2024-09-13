from django.shortcuts import render,get_list_or_404,redirect,get_object_or_404
from django.contrib.auth import login,authenticate,logout

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from . import models

def movie_list(request,category_slug=None):
    category = None
    categories = models.Category.objects.all()
    movies = models.Movies.objects.all()
    if category_slug:
        category = get_list_or_404(models.Category,slug=category_slug)
        movies=movies.filter(category=category)
    return render(request,'home.html',{
        'category':category,
        'categories':categories,
        'movies':movies,
    })

def home(request):
    return render(request, 'home.html')
from django.shortcuts import render



def view(request):
    return render(request, 'viewfim.html')

def films(request):
    return render(request, 'films.html')

def login(request):
    return render(request, 'login.html')
def detail(request):
    return render(request, 'movie_detail.html')

def movie_detail(request, id):
    movie = get_object_or_404(models.Movies, id=id)  # Filmni bazadan olamiz
    return render(request, 'movie_detail.html',  {'movie': movie})  # Shablonga uzatamiz


