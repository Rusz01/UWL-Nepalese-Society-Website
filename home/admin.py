from django.contrib import admin
from home.models import RecentEvent, Event, Contact, Members, Member_detail, Blog

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

class BlogAdmin(admin.ModelAdmin):
    list_display = ('heading', 'authorname', 'status', 'blog_created_date')
    list_filter = ('status', 'authorname')
    search_fields = ('heading', 'caption')
    
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ['status']  # Non-superusers can't change the status
        return self.readonly_fields

    def approve_post(self, request, queryset):
        queryset.update(status='approved')
    approve_post.short_description = "Approve selected posts"

    def reject_post(self, request, queryset):
        queryset.update(status='rejected')
    reject_post.short_description = "Reject selected posts"

    actions = [approve_post, reject_post]

admin.site.register(Blog, BlogAdmin)


