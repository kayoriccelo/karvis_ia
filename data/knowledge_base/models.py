from django.db import models


class KnowledgeBase(models.Model):
    intentions = models.ManyToManyField('intention.Intention', related_name='knowledge_bases')
    description = models.TextField()

    class Meta:
        db_table = 'knowledge_base'
        verbose_name = 'Knowledge Base'
        verbose_name_plural = 'Knowledge Bases'
