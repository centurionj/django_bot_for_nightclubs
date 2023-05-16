from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

import os

# Create your models here.

class Day(models.Model):
    day_of_weak = models.CharField('День недели', max_length=15)

    def __str__(self):
        return self.day_of_weak

    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'
        ordering = ['id']

class Perfomace(models.Model):
    preview = models.FileField('Превью', default='Превью', null=True)
    title = models.TextField('Описание', default='Описание')
    date = models.DateTimeField('Дата мероприятия')
    club = models.ForeignKey('Club', on_delete=models.PROTECT)
    which_day_of_weak = models.ForeignKey(Day, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['date']

class Club(models.Model):
    name = models.CharField('Название клуба', max_length=50, default='Название клуба')
    qr_code = models.BooleanField('Есть QrCode?', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клуб'
        verbose_name_plural = 'Клубы'
        ordering = ['name']

class Order(models.Model):
    name_sername = models.CharField('Имя Фамилия', max_length=50, default='Имя Фамилия')
    date = models.DateField()
    club = models.CharField('Название клуба', max_length=50, default='Название клуба')

    def __str__(self):
        return self.name_sername

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'
        ordering = ['date']

@receiver(pre_delete, sender=Perfomace)
def delete_file(sender, instance, **kwargs):
    if instance.preview:
        try:
            os.remove(instance.preview.path)
        except:
            pass
