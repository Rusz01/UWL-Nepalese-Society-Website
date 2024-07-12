from django.shortcuts import get_object_or_404, render
from home.models import Event, Members, RecentEvent, Contact, Member_detail
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings


# Create your views here.
def home(request):
   pics=Event.objects.all().order_by('-EventCreatedDate')
   rimage = RecentEvent.objects.all().order_by('-RecentEventCreatedDate')
   return render(request, 'index.html', {"pics": pics, "rimage": rimage})

def event(request):
   pics=Event.objects.all().order_by('-EventCreatedDate')
   rimage = RecentEvent.objects.all().order_by('-RecentEventCreatedDate')
   return render(request, 'event.html', {"pics": pics, "rimage": rimage})

def contact(request):
   if request.method=="POST":
      name = request.POST['name']
      email = request.POST['email']
      number = request.POST['number']
      message = request.POST['message']
      ins = Contact(name=name, email=email, number=number, message=message)
      ins.save()

   return render(request, 'contact.html')

def members(request):
    pics = Member_detail.objects.all()
    year = Members.objects.all()
    return render(request, 'members.html',{"pics":pics, "year": year})

def singlePageEvent(request, image_id):
   pics=Event.objects.all()
   single_event = get_object_or_404(RecentEvent, pk=image_id)
   return render(request, 'single-page-event.html',{'single_event': single_event, "pics":pics})

def allRecentEvents(request):
   rimage= RecentEvent.objects.all().order_by('-RecentEventCreatedDate')
   paginator = Paginator(rimage, 2)  # Show 3 events per page
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
   return render(request, 'all-recent-events.html', {'page_obj': page_obj})

# Developer Page
def developer(request):
   return render(request, 'developer.html')

# Board Member Single Page
def memberSingle(request, image_id):
   member = get_object_or_404(Member_detail, pk=image_id)
   return render(request, 'member-single.html', {'member': member})
   