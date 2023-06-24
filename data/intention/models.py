from django.db import models


class Intention(models.Model):
    description = models.TextField()
    active = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        db_table = 'intention'
        verbose_name = 'Intention'
        verbose_name_plural = 'Intentions'

    def __str__(self):
        return self.description
