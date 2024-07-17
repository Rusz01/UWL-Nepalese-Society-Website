from django.contrib import admin
from home.models import Event
from home.models import RecentEvent
from home.models import RecentEventComplete

class RecentEventCompleteAdmin(admin.StackedInline):
    model = RecentEventComplete

# Register your models here.
admin.site.register(Event)

@admin.register(RecentEvent)
class RecentEventAdmin(admin.ModelAdmin):
    inlines = [RecentEventCompleteAdmin]

    class Meta:
        model = RecentEvent

@admin.register(RecentEventComplete)        
class RecentEventCompleteAdmin(admin.ModelAdmin):
    pass