
from django.http import HttpResponse
from django.conf import settings
from home.models import Contact
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
# from home.models import Event, Members, RecentEvent, Contact, Member_detail
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .form import ContactForm
from django.contrib import messages


# Create your views here.
def home(request):
   return render(request, 'index.html')

def event(request):
   return render(request, 'event.html')

def Contact_view(request):
   if request.method == 'POST':
      form = ContactForm(request.POST)
      if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            number = form.cleaned_data['number']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Example: Send an email with the form data
            subject = 'Contact Form Submission'
            message_body = f'Name: {name}\nPhone Number: {number}\nEmail: {email}\nMessage: {message}'
            send_mail(
               subject,
               message_body,
               settings.EMAIL_HOST_USER, #EMAIL OF SENDER
               [email],
               fail_silently=False,
            )
            ins = Contact(name=name, email=email, number=number, message=message)
            ins.save()
            messages.success(request, 'Successfully Submitted')
      else:
         messages.error(request, 'Submission failed')
   else:
      form = ContactForm()
   return render(request, 'contact.html', {'form': form})

def members(request):
   return render(request, 'members.html')

   pics = Member_detail.objects.all()
   year = Members.objects.all()
   return render(request, 'members.html',{"pics":pics, "year": year})


def singlePageEvent(request):
   return render(request, 'single-page-event.html')

def allRecentEvents(request):
   return render(request, 'all-recent-events.html')