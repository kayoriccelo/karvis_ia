# Generated by Django 2.2.12 on 2023-06-25 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0003_auto_20230625_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabulary',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, 'Apresentar-se'), (2, 'Oferecer ajudar'), (3, 'Que informação deseja'), (5, 'Não entendi, fale novamente'), (6, 'Continuo sem entender, repita'), (7, 'Precisa de algo mais'), (8, 'Prazer poder lhe-ajudar'), (9, 'Eu que agradeço em ajudar'), (10, 'Não entendi o que você disse'), (11, 'Não sei fazer isso.'), (11, 'Não sei nada sobre isso.')], null=True),
        ),
    ]