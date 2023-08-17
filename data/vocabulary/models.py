from django.db import models

from .choices import C_TYPE_VOCABULARY


class Vocabulary(models.Model):
    description = models.TextField()
    intentions = models.ManyToManyField('intention.Intention', related_name='dialogs', blank=True)
    type = models.IntegerField(choices=C_TYPE_VOCABULARY, null=True, blank=True)
    active = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        db_table = 'vocabulary'
        verbose_name = 'Vocabulary'
        verbose_name_plural = 'Vocabularies'

    def __str__(self):
        return f'{self.get_type_display()}'
