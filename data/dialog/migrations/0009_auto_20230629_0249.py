# Generated by Django 2.2.12 on 2023-06-29 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dialog', '0008_auto_20230626_0312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dialogresponse',
            name='dialog_command',
        ),
        migrations.DeleteModel(
            name='DialogCommand',
        ),
    ]
