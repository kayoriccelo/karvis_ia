# Generated by Django 2.2.12 on 2023-06-25 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dialog', '0003_auto_20230625_0541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dialogcommand',
            name='dialog_response',
        ),
        migrations.RemoveField(
            model_name='dialogquestion',
            name='dialog_response',
        ),
        migrations.AddField(
            model_name='dialogresponse',
            name='dialog_command',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dialogs_response', to='dialog.DialogCommand'),
        ),
        migrations.AddField(
            model_name='dialogresponse',
            name='dialog_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dialogs_response', to='dialog.DialogQuestion'),
        ),
    ]