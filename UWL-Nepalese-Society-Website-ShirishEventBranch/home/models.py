from django.db import models
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
