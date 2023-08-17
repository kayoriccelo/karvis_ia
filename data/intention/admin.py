from django.contrib import admin

from .models import Intention


@admin.register(Intention)
class IntentionAdmin(admin.ModelAdmin):
    fields = ('description', 'type', 'active', )
    search_fields = ('description', 'type', 'active', )
    list_display = ('description', 'type', 'active', )
