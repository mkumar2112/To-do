# Import required Module to run our server...

from django.contrib import admin
from django.urls import path
from Home import views
from .views import list

# Giving path to our web pages to  perform task as they are builded...
urlpatterns = [
    path('', views.home, name='Home'),
    path('home', views.home, name='Home'),
    path('login', views.loginuser, name='Login User Page'),
    path('create_user', views.create_user, name='Create User Page'),
    path('app', views.app, name='Note Page'),
    path('add_note', views.add_note, name='Add Note Page'),
    path('logout', views.logoutuser, name='Login User Page'),
    path('contact',views.contact, name='Contact Page'),
    path('tasks/', list.as_view(),name='tasks'),
    path('thanks', views.thanks , name='show'),
]
