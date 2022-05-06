from django.contrib import admin

from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ["id", "content_type"]


    class Meta: 
        model = Note


admin.site.register(Note, NoteAdmin)
