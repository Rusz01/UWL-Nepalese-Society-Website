from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
#    URLS for Pages
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('event', views.event, name='event'),
    path('members', views.members, name='members'),

    # For single page event
    path('singlePageEvent', views.singlePageEvent, name='singlePageEvent'),
]