# Generated by Django 2.2.12 on 2023-06-24 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('intention', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('type', models.IntegerField(blank=True, choices=[(1, 'Apresentar-se'), (2, 'Oferecer ajudar'), (3, 'Que informação deseja'), (5, 'Não entendi, fale novamente'), (6, 'Continuo sem entender, repita'), (7, 'Precisa de algo mais'), (8, 'Prazer poder lhe-ajudar'), (9, 'Eu que agradeço em ajudar'), (10, 'Não entendi o que você disse'), (11, 'Não sei fazer isso.')], null=True)),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('intentions', models.ManyToManyField(related_name='dialogs', to='intention.Intention')),
            ],
            options={
                'verbose_name': 'Vocabulary',
                'verbose_name_plural': 'Vocabularies',
                'db_table': 'vocabulary',
            },
        ),
    ]
