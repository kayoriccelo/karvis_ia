from django.contrib import admin

from .models import Dialog, DialogQuestion, DialogResponse


@admin.register(Dialog)
class DialogAdmin(admin.ModelAdmin):
    fields = ('status', 'dialogs', )
    search_fields = ('date', 'status', )
    list_display = ('date', 'status', )


@admin.register(DialogQuestion)
class DialogQuestionAdmin(admin.ModelAdmin):
    fields = ('dialog', 'question', 'intention', 'vocabulary', 'author', )
    search_fields = ('dialog', 'question', 'intention', 'vocabulary', 'author', 'date')
    list_display = ('dialog', 'question', 'intention', 'vocabulary', 'author', 'date')
    raw_id_fields = ('dialog', 'intention', 'vocabulary', )


@admin.register(DialogResponse)
class DialogResponseAdmin(admin.ModelAdmin):
    fields = ('dialog_question', 'response', 'intention', 'vocabulary', 'knowledge_base', 'author',)
    search_fields = ('dialog_question', 'response', 'intention', 'vocabulary', 'knowledge_base', 'author', 'date')
    list_display = ('dialog_question', 'response', 'intention', 'vocabulary', 'knowledge_base', 'author', 'date')
    raw_id_fields = ('dialog_question', 'intention', 'vocabulary', 'knowledge_base')
