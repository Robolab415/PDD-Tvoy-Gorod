from django.contrib import admin
from .models import Ticket, Photo

class PhotoInline(admin.TabularInline):
    model = Photo

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('number', 'question')
    inlines = [PhotoInline]

@admin.register(Photo)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'photo')
