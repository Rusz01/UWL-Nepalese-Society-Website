from django.shortcuts import get_object_or_404, render, redirect
from home.form import ContactForm
from home.models import Event, Members, RecentEvent, Contact, Member_detail, RecentEventComplete

from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from .models import Blog
from .forms import BlogForm  # Assuming a form for blog submission
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
   pics=Event.objects.all().order_by('-EventCreatedDate')
   rimage = RecentEvent.objects.all().order_by('-RecentEventCreatedDate')
   return render(request, 'index.html', {"pics": pics, "rimage": rimage})

def event(request):
   pics=Event.objects.all().order_by('-EventCreatedDate')
   rimage = RecentEvent.objects.all().order_by('-RecentEventCreatedDate')
   return render(request, 'event.html', {"pics": pics, "rimage": rimage})

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
    pics = Member_detail.objects.all()
    year = Members.objects.all()
    return render(request, 'members.html',{"pics":pics, "year": year})

def singlePageEvent_view(request, id):
   pics=Event.objects.all().order_by('-EventCreatedDate')
   rEvent = get_object_or_404(RecentEvent, id=id)
   photos = RecentEventComplete.objects.filter(rEvent=rEvent)
   return render(request, 'single-page-event.html',{'rEvent':rEvent,'photos':photos, "pics": pics})

def allRecentEvents(request):
    rimage = RecentEvent.objects.all().order_by('-RecentEventCreatedDate')
    paginator = Paginator(rimage, 2)  # Show 2 events per page
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
   
# Blog Page
def blog(request):
    featured_articles = Blog.objects.filter(status='approved')[:5]  # Only show approved articles
    return render(request, 'blog.html', {'featured_articles': featured_articles})

# Single blog page
def singleblog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, status='approved')  # Ensure only approved blogs can be accessed
    featured_articles = Blog.objects.filter(status='approved')[:5]  # Only show approved articles
    return render(request, 'single-blog.html', {'blog': blog, 'featured_articles': featured_articles})

# Submit a new blog post (only for logged-in users)
@login_required
def submit_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.authorname = request.user.username  # Set the author as the logged-in user
            blog_post.status = 'pending'  # Automatically set the status to pending
            blog_post.save()
            return redirect('blog')  # Redirect to blog listing or a success page
    else:
        form = BlogForm()
    return render(request, 'submit_blog.html', {'form': form})
