from django.shortcuts import get_object_or_404, render
from home.models import Event
from home.models import RecentEvent
from django.core.paginator import Paginator
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
   return render(request, 'contact.html')

def members(request):
   return render(request, 'members.html')

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
