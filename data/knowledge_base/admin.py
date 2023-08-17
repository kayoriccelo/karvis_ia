from django.contrib import admin

from .models import KnowledgeBase


@admin.register(KnowledgeBase)
class KnowledgeBasetAdmin(admin.ModelAdmin):
    fields = ('intentions', 'description',)
    search_fields = ('intentions', 'description',)
    list_display = ('description',)
