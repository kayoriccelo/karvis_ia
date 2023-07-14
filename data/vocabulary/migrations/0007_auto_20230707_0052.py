# Generated by Django 2.2.12 on 2023-07-07 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0006_auto_20230706_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabulary',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, 'Apresentar-se'), (2, 'Oferecer ajudar'), (3, 'Que informação deseja'), (5, 'Não entendi, fale novamente'), (6, 'Continuo sem entender, repita'), (7, 'Precisa de algo mais'), (8, 'Prazer poder lhe-ajudar'), (9, 'Eu que agradeço em ajudar'), (10, 'Não entendi o que você disse'), (11, 'Não sei fazer isso'), (12, 'Não sei nada sobre isso'), (13, 'Alerta antes de criar intenção'), (14, 'What Intent Do You Want To Create?'), (15, 'Qual tipo de intençao'), (16, 'What add some more intention?'), (17, 'Qual conhecimento deseja ensinar'), (18, 'Want To Add a New Intent?'), (19, 'What Do You Want To Search In ChatGPT?'), (20, 'How Many Minutes To Informe Knowledge?'), (21, 'What To Inform Knowledge?'), (22, 'What You Want Search ChatGPT'), (23, 'Thanks For The New Knowledge'), (24, 'I Found The Following Information'), (25, 'Confirms This Information For Knowledge?')], null=True),
        ),
    ]