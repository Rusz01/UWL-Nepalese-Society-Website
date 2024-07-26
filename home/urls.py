from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
#    URLS for Pages
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('event/', views.event, name='event'),
    path('members/', views.members, name='members'),
    path('developer', views.developer, name='developer'),
    path('blog/', views.blog, name='blog'),

    # For single blog page
    path('single-blog//<int:blog_id>/', views.singleblog, name='single-blog'),

    # For single member page
    path('member/<int:image_id>/', views.memberSingle, name='member-single'),

    # For single event page 
    path('image/<int:image_id>/', views.singlePageEvent, name='singlePageEvent'),

    # For all recent event page
    path('allRecentEvents', views.allRecentEvents, name='allRecentEvents'),
]