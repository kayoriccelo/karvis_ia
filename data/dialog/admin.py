from django.contrib import admin

from .models import Dialog, DialogQuestion, DialogCommand, DialogResponse


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


@admin.register(DialogCommand)
class DialogCommandAdmin(admin.ModelAdmin):
    fields = ('dialog', 'command', 'intention', 'author', )
    search_fields = ('dialog', 'command', 'intention', 'author', 'date')
    list_display = ('dialog', 'command', 'intention', 'author', 'date')
    raw_id_fields = ('dialog', 'intention', )


@admin.register(DialogResponse)
class DialogResponseAdmin(admin.ModelAdmin):
    fields = (
        'dialog_question', 'dialog_command', 'response', 'intention', 'vocabulary', 'knowledge_base', 'author',
    )
    search_fields = (
        'dialog_question', 'dialog_command', 'response', 'intention', 'vocabulary', 'knowledge_base', 'author', 'date'
    )
    list_display = (
        'dialog_question', 'dialog_command', 'response', 'intention', 'vocabulary', 'knowledge_base', 'author', 'date'
    )
    raw_id_fields = ('dialog_question', 'dialog_command', 'intention', 'vocabulary', 'knowledge_base')
