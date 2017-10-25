# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Bookmark, Tag

# zafezo qwert123456 

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'owner', 'is_public', 'date_updated')
    list_editable = ('is_public',)
    list_filter = ('is_public', 'owner__username')
    search_fields = ['url', 'title', 'desciption']
    readonly_fields = ('date_created', 'date_updated')

admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Tag)
