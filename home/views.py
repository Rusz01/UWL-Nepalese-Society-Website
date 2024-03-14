from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from home.models import Contact
# from django.core.mail import send_mail
# Create your views here.
def home(request):
   return render(request, 'index.html')

def event(request):
   return render(request, 'event.html')

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
   return render(request, 'members.html')

def singlePageEvent(request):
   return render(request, 'single-page-event.html')

def allRecentEvents(request):
   return render(request, 'all-recent-events.html')