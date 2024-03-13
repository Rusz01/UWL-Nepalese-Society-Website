from django.shortcuts import get_object_or_404, render
from home.models import Event
from home.models import RecentEvent
# Create your views here.
def home(request):
   pics=Event.objects.all()
   rimage = RecentEvent.objects.all()
   return render(request, 'index.html', {"pics": pics, "rimage": rimage})

def event(request):
   pics=Event.objects.all()
   rimage = RecentEvent.objects.all()
   return render(request, 'event.html', {"pics": pics, "rimage": rimage})

def contact(request):
   return render(request, 'contact.html')

def members(request):
   return render(request, 'members.html')

def singlePageEvent(request, image_id):
   pics=Event.objects.all()
   single_event = get_object_or_404(RecentEvent, pk=image_id)
   return render(request, 'single-page-event.html',{'single_event': single_event, "pics":pics})

def allRecentEvents(request):
   rimage= RecentEvent.objects.all()
   return render(request, 'all-recent-events.html',{"rimage": rimage})
