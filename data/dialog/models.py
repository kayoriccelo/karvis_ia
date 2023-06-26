from django.db import models

from .choices import C_AUTHOR_DIALOG, C_STATUS_DIALOG, STATUS_DIALOG_STARTED


class Dialog(models.Model):
    dialogs = models.ManyToManyField('self', related_name='dialogs')
    status = models.IntegerField(choices=C_STATUS_DIALOG, default=STATUS_DIALOG_STARTED)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dialog'
        verbose_name = 'Dialog'
        verbose_name_plural = 'Dialogs'

    def __str__(self):
        return f'{self.date.strftime("%d/%m/%Y %H:%M:%S")} - {self.get_status_display()}'


class DialogCommand(models.Model):
    dialog = models.ForeignKey(Dialog, related_name='dialogs_command', on_delete=models.CASCADE)
    command = models.TextField(null=True, blank=True)
    intention = models.ForeignKey(
        'intention.Intention', related_name='dialogs_command', null=True, blank=True, on_delete=models.PROTECT
    )
    author = models.IntegerField(choices=C_AUTHOR_DIALOG)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dialog_command'
        verbose_name = 'Dialog Command'
        verbose_name_plural = 'Dialogs Command'

    def __str__(self):
        return f'{self.date.strftime("%d/%m/%Y %H:%M:%S")} - {self.get_author_display()} - {self.intention}'


class DialogQuestion(models.Model):
    dialog = models.ForeignKey(Dialog, related_name='dialogs_question', on_delete=models.CASCADE)
    question = models.TextField(null=True, blank=True)
    intention = models.ForeignKey(
        'intention.Intention', related_name='dialogs_question', null=True, blank=True, on_delete=models.PROTECT
    )
    vocabulary = models.ForeignKey(
        'vocabulary.Vocabulary', related_name='dialogs_question', null=True, blank=True, on_delete=models.PROTECT
    )
    author = models.IntegerField(choices=C_AUTHOR_DIALOG)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dialog_question'
        verbose_name = 'Dialog Question'
        verbose_name_plural = 'Dialogs Question'

    def __str__(self):
        return f'{self.date.strftime("%d/%m/%Y %H:%M:%S")} - {self.get_author_display()} - {self.intention} - {self.vocabulary}'


class DialogResponse(models.Model):
    dialog_question = models.ForeignKey(
        DialogQuestion, related_name='dialogs_response', null=True, blank=True, on_delete=models.CASCADE
    )
    dialog_command = models.ForeignKey(
        DialogCommand, related_name='dialogs_response', null=True, blank=True, on_delete=models.CASCADE
    )
    response = models.TextField(null=True, blank=True)
    intention = models.ForeignKey(
        'intention.Intention', related_name='dialogs_response', null=True, blank=True, on_delete=models.PROTECT
    )
    vocabulary = models.ForeignKey(
        'vocabulary.Vocabulary', related_name='dialogs_response', null=True, blank=True, on_delete=models.PROTECT
    )
    knowledge_base = models.ForeignKey(
        'knowledge_base.KnowledgeBase', related_name='dialogs_response', null=True, blank=True, on_delete=models.PROTECT
    )
    author = models.IntegerField(choices=C_AUTHOR_DIALOG)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dialog_response'
        verbose_name = 'Dialog Response'
        verbose_name_plural = 'Dialogs Response'

    def __str__(self):
        return f'{self.date.strftime("%d/%m/%Y %H:%M:%S")} - {self.get_author_display()} - {self.intention} - {self.vocabulary} - {self.knowledge_base}'
