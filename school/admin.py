from django.contrib import admin
from .models import Announcement, ContactMessage, Application


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')
    ordering = ('-date_posted',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    ordering = ('-created_at',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'learner_name',
        'learner_surname',
        'province',
        'status',
        'submitted_at'
    )
    list_filter = ('status', 'province')
    search_fields = ('learner_name', 'learner_surname', 'id_number')
    ordering = ('-submitted_at',)