import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
from tinymce.models import HTMLField
# Create your models here.
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    image=models.ImageField(upload_to="image")
    heading = models.CharField(max_length=100,  blank=True, null=True)
    caption=HTMLField()
    booking_link = models.URLField(blank=True, null=True)
    EventCreatedDate = models.DateTimeField(auto_now_add=True, null = True)
    def __str__(self):
        return self.heading

class RecentEvent(models.Model):
    id = models.AutoField(primary_key=True)
    image=models.ImageField(upload_to="recentimage")
    heading = models.CharField(max_length=100,  blank=True, null=True)
    caption=HTMLField()
    RecentEventCreatedDate = models.DateTimeField(auto_now_add=True, null = True)
    def __str__(self):
        return self.heading

# Contact
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    number = models.CharField(max_length=15)    
    message = models.TextField()
    
    def __str__ (self):
        return self.name + " - " + self.email


# creating a class "Members" for date and recently added which provides time and day when updated 
class Members(models.Model):
    member_year = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateTimeField("Date")
    def __str__(self):
        return self.member_year
    @admin.display(
        boolean=True,
        ordering="date",
        description='Recently Added',
    )
    def was_recently_added(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date <= now
    
    # Ordering member_year in descending order
    class Meta:
        ordering = ['-member_year']  


# creating a class "List" to insert members details 
class Member_detail(models.Model):

    # code to insert image, name, title, details and social links
    id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Members, on_delete=models.CASCADE)

    image = models.ImageField(upload_to="image")
    name = models.CharField(max_length=25, blank=True, null=True)
    title = models.CharField(max_length=25, blank=True, null=True)
    date_year = models.CharField(max_length=20, blank=True, null=True)
    details_text = models.TextField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedln_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
# creating a model for blog
class Blog(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="image")
    heading = models.CharField(max_length=100, blank=True, null=True)
    caption = HTMLField()
    authorname = models.CharField(max_length=50, blank=True, null=True)
    authorname_hyperlink = models.URLField(blank=True, null=True)
    blog_created_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  # New status field

    def __str__(self):
        return self.heading


 
class RecentEventComplete(models.Model):
    rEvent = models.ForeignKey(RecentEvent, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to ='recentimage')

    def __str__(self):
        return self.rEvent.heading
