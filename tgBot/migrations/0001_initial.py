# Generated by Django 4.2 on 2023-05-05 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Название клуба', max_length=50, verbose_name='Название клуба')),
                ('qr_code', models.BooleanField(default=True, max_length=50, verbose_name='Есть QrCode?')),
            ],
            options={
                'verbose_name': 'Клуб',
                'verbose_name_plural': 'Клубы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_weak', models.CharField(max_length=15, verbose_name='День недели')),
            ],
            options={
                'verbose_name': 'День недели',
                'verbose_name_plural': 'Дни недели',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Perfomace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview', models.ImageField(default='Превью', upload_to='', verbose_name='Превью')),
                ('title', models.TextField(default='Описание', verbose_name='Описание')),
                ('date', models.DateTimeField(verbose_name='Дата мероприятия')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tgBot.club')),
                ('which_day_of_weak', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tgBot.day')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_sername', models.CharField(default='Имя Фамилия', max_length=50, verbose_name='Имя Фамилия')),
                ('date', models.DateTimeField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tgBot.club')),
            ],
            options={
                'verbose_name': 'Отчет',
                'verbose_name_plural': 'Отчеты',
            },
        ),
    ]
