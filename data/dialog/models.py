from django.db import models

from .choices import C_AUTHOR_DIALOG, C_STATUS_DIALOG, STATUS_DIALOG_STARTED


class Dialog(models.Model):
    dialogs = models.ManyToManyField('self', related_name='dialogs')
    status = models.IntegerField(choices=C_STATUS_DIALOG, default=STATUS_DIALOG_STARTED)

    class Meta:
        db_table = 'dialog'
        verbose_name = 'Dialog'
        verbose_name_plural = 'Dialogs'


class DialogResponse(models.Model):
    response = models.TextField(null=True, blank=True)
    vocabulary = models.ForeignKey(
        'vocabulary.Vocabulary', related_name='dialogs_response', null=True, blank=True, on_delete=models.PROTECT
    )
    author = models.IntegerField(choices=C_AUTHOR_DIALOG)

    class Meta:
        db_table = 'dialog_response'
        verbose_name = 'Dialog Response'
        verbose_name_plural = 'Dialogs Response'


class DialogCommand(models.Model):
    dialog = models.ForeignKey(Dialog, related_name='dialogs_command', on_delete=models.CASCADE)
    dialog_response = models.ForeignKey(DialogResponse, related_name='dialogs_command', on_delete=models.PROTECT)
    command = models.TextField(null=True, blank=True)
    intention = models.ForeignKey(
        'intention.Intention', related_name='dialogs_command', null=True, blank=True, on_delete=models.PROTECT
    )
    author = models.IntegerField(choices=C_AUTHOR_DIALOG)

    class Meta:
        db_table = 'dialog_command'
        verbose_name = 'Dialog Command'
        verbose_name_plural = 'Dialogs Command'


class DialogQuestion(models.Model):
    dialog = models.ForeignKey(Dialog, related_name='dialogs_question', on_delete=models.CASCADE)
    dialog_response = models.ForeignKey(DialogResponse, related_name='dialogs_question', on_delete=models.PROTECT)
    question = models.TextField(null=True, blank=True)
    intention = models.ForeignKey(
        'intention.Intention', related_name='dialogs_question', null=True, blank=True, on_delete=models.PROTECT
    )
    author = models.IntegerField(choices=C_AUTHOR_DIALOG)

    class Meta:
        db_table = 'dialog_question'
        verbose_name = 'Dialog Question'
        verbose_name_plural = 'Dialogs Question'
