import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.

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


# creating a class "List" to insert members details 
class Member_detail(models.Model):

    # code to insert image, name, title, details and social links
    id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Members, on_delete=models.CASCADE)

    image = models.ImageField(upload_to="image")
    name = models.CharField(max_length=25, blank=True, null=True)
    title = models.CharField(max_length=25, blank=True, null=True)
    date_year = models.CharField(max_length=20, blank=True, null=True)
    details_text = models.CharField(max_length=150, blank=True, null=True)
    socials_link = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.name
    

