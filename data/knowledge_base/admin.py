from django.contrib import admin

from .models import KnowledgeBase


@admin.register(KnowledgeBase)
class KnowledgeBasetAdmin(admin.ModelAdmin):
    fields = ('intention', 'description',)
    search_fields = ('intention', 'description',)
    list_display = ('description',)
