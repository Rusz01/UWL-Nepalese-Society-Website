from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
#    URLS for Pages
    path('', views.home, name='home'),
    path('Contact/', views.Contact_view, name='Contact'),
    path('event', views.event, name='event'),
    path('members', views.members, name='members'),

    # For single event page
    path('singlePageEvent', views.singlePageEvent, name='singlePageEvent'),

    # For all recent event page
    path('allRecentEvents', views.allRecentEvents, name='allRecentEvents'),
]