# Generated by Django 2.2.12 on 2023-06-24 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vocabulary', '0001_initial'),
        ('intention', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Started'), (2, 'Progress'), (3, 'Pending'), (4, 'Finished')], default=1)),
                ('dialogs', models.ManyToManyField(related_name='_dialog_dialogs_+', to='dialog.Dialog')),
            ],
            options={
                'verbose_name': 'Dialog',
                'verbose_name_plural': 'Dialogs',
                'db_table': 'dialog',
            },
        ),
        migrations.CreateModel(
            name='DialogResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField(blank=True, null=True)),
                ('author', models.IntegerField(choices=[(1, 'AI'), (2, 'User')])),
                ('vocabulary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dialogs_response', to='vocabulary.Vocabulary')),
            ],
            options={
                'verbose_name': 'Dialog Response',
                'verbose_name_plural': 'Dialogs Response',
                'db_table': 'dialog_response',
            },
        ),
        migrations.CreateModel(
            name='DialogQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True)),
                ('author', models.IntegerField(choices=[(1, 'AI'), (2, 'User')])),
                ('dialog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dialogs_question', to='dialog.Dialog')),
                ('dialog_response', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dialogs_question', to='dialog.DialogResponse')),
                ('intention', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dialogs_question', to='intention.Intention')),
            ],
            options={
                'verbose_name': 'Dialog Question',
                'verbose_name_plural': 'Dialogs Question',
                'db_table': 'dialog_question',
            },
        ),
        migrations.CreateModel(
            name='DialogCommand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.TextField(blank=True, null=True)),
                ('author', models.IntegerField(choices=[(1, 'AI'), (2, 'User')])),
                ('dialog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dialogs_command', to='dialog.Dialog')),
                ('dialog_response', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dialogs_command', to='dialog.DialogResponse')),
                ('intention', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dialogs_command', to='intention.Intention')),
            ],
            options={
                'verbose_name': 'Dialog Command',
                'verbose_name_plural': 'Dialogs Command',
                'db_table': 'dialog_command',
            },
        ),
    ]