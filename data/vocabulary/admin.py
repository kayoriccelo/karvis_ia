from django.contrib import admin

from .models import Vocabulary


@admin.register(Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    fields = ('description', 'type', 'active', 'intentions', )
    search_fields = ('description', 'intentions', 'type', )
    list_display = ('description', 'type', 'active', )
