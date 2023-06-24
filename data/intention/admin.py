from django.contrib import admin

from .models import Intention


@admin.register(Intention)
class IntentionAdmin(admin.ModelAdmin):
    fields = ('description', 'active', )
    search_fields = ('description', 'active', )
    list_display = ('description', 'active', )
