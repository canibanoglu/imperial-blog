from django.contrib import admin
from kindle_notes.models import Book, Note

class NoteAdmin(admin.ModelAdmin):
    ordering = ['-date']


admin.site.register(Book)
admin.site.register(Note, NoteAdmin)
