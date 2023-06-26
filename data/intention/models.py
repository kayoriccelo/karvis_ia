from django.db import models

from data.intention.choices import C_TYPE_INTENTION


class Intention(models.Model):
    description = models.TextField()
    active = models.BooleanField(default=True, null=True, blank=True)
    type = models.IntegerField(choices=C_TYPE_INTENTION, null=True, blank=False)

    class Meta:
        db_table = 'intention'
        verbose_name = 'Intention'
        verbose_name_plural = 'Intentions'

    def __str__(self):
        return self.description
