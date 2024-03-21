from django.contrib import admin
from home.models import Event
from home.models import RecentEvent
# Register your models here.
admin.site.register(Event)
admin.site.register(RecentEvent)
