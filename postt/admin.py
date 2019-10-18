# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import postt




class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'publishing_date']
    list_display_links = ['title', 'publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['title', 'content']

    class Meta:
        model = postt



admin.site.register(postt, PostAdmin)
