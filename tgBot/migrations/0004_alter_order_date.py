# Generated by Django 4.2 on 2023-05-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgBot', '0003_alter_club_qr_code_alter_perfomace_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(),
        ),
    ]
