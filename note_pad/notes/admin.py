from django.contrib import admin
from .models import *

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'created_at', 'updated_at']
    search_fields = ['title', 'text']
    list_filter = ['created_at', 'updated_at']
# Register your models here.
