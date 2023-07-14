# Generated by Django 2.2.12 on 2023-07-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intention', '0004_auto_20230629_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intention',
            name='type',
            field=models.IntegerField(choices=[(1, 'Hi AI'), (2, 'Goodbye'), (3, 'Good night'), (4, 'Information'), (5, 'I Need Information'), (7, 'Confirmation'), (8, 'Negation'), (9, 'Farewell'), (10, 'Create'), (11, 'Create Knowledge Base')], null=True),
        ),
    ]
