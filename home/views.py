from django.shortcuts import render

# Create your views here.
def home(request):
   return render(request, 'index.html')

def event(request):
   return render(request, 'event.html')

def contact(request):
   return render(request, 'contact.html')

def members(request):
   return render(request, 'members.html')

def singlePageEvent(request):
   return render(request, 'single-page-event.html')

def allRecentEvents(request):
   return render(request, 'all-recent-events.html')