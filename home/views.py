from django.shortcuts import get_object_or_404, render
from home.models import Event
from home.models import RecentEvent
from home.models import RecentEventComplete
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

def singlePageEvent_view(request, id):
   rEvent = get_object_or_404(RecentEvent, id=id)
   photos = RecentEventComplete.objects.filter(rEvent=rEvent)
   return render(request, 'single-page-event.html',{'rEvent':rEvent,'photos':photos})

def allRecentEvents(request):
   rimage= RecentEvent.objects.all().order_by('-RecentEventCreatedDate')
   paginator = Paginator(rimage, 2)  # Show 3 events per page
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
   return render(request, 'all-recent-events.html',{'rimage':rimage, 'page_obj': page_obj})
