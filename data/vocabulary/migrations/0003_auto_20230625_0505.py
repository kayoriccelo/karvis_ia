# Generated by Django 2.2.12 on 2023-06-25 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0002_auto_20230625_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabulary',
            name='intentions',
            field=models.ManyToManyField(blank=True, related_name='dialogs', to='intention.Intention'),
        ),
    ]