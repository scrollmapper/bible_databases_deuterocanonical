from django.contrib import admin
from books.models import *
# Register your models here.



class BookAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name',]    
admin.site.register(Book, BookAdmin)

class VerseAdmin(admin.ModelAdmin):
    list_display = ['position', 'book', 'chapter_str', 'verse_str', 'text']
    ordering = ['position']
admin.site.register(Verse, VerseAdmin)
