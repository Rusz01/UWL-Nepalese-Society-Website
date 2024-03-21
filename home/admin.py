from django.contrib import admin
from home.models import Event
from home.models import RecentEvent, Event, Contact, Members, Member_detail

# Register your models here.

# Event and Recent Event
admin.site.register(Event)
admin.site.register(RecentEvent)

# Contact admin
admin.site.register(Contact)

# class to modify the lines
class ChoiceInline(admin.StackedInline):
    model = Member_detail
    extra = 1

# class for showing members and their lists inline
class Member_detail(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["member_year"]}),
        ("Date information", {"fields": ["date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

    list_display = ["member_year", "date", "was_recently_added"]
    list_filter = ["date"]
    search_fields = ["member_year"]

admin.site.register(Members,  Member_detail)
