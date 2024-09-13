from django.urls import path
from . import views
urlpatterns = [
    path('',views.movie_list,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.login,name='register'),
    path('movies/<int:id>/', views.movie_detail, name='movie_detail'),
    path('film',views.view, name='viewfilm'),
    path('films/',views.films, name='films')
]