from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
#    URLS for Pages
    path('', views.home, name='home'),
    path('Contact/', views.Contact_view, name='Contact'),
    path('event/', views.event, name='event'),
    path('members/', views.members, name='members'),
    path('developer', views.developer, name='developer'),
    path('blog/', views.blog, name='blog'),
    path('single-blog/', views.singleBlog, name='single-blog'),
    path('member-single', views.memberSingle, name='memberSingle'),



    # For single event page 
    path('<int:id>/', views.singlePageEvent_view, name='singlePageEvent'),

    # For all recent event page
    path('allRecentEvents', views.allRecentEvents, name='allRecentEvents'),
]