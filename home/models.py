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

#class EventImage(models.Model):
   # event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)



class RecentEvent(models.Model):
    heading = models.CharField(max_length=100,  blank=True, null=True)
    id = models.AutoField(primary_key=True)
    image=models.FileField(blank=True)
    caption=HTMLField()
    RecentEventCreatedDate = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.heading
 
class RecentEventComplete(models.Model):
    rEvent = models.ForeignKey(RecentEvent, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to ='recentimage')

    def __str__(self):
        return self.rEvent.heading