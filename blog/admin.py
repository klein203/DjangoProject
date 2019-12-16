from django.contrib import admin
from .models import Category, Tag, Entry


# Register your models here.
class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'visiting', 'create_time', 'update_time']


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Entry, EntryAdmin)