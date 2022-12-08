from django.db import models


# Create your models here.

class IceCream(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        default='',
        editable=True,
        max_length=100

    )
    flavour = models.CharField(
        verbose_name='Вкус',
        default='',
        editable=True,
        max_length=100

    )

    price = models.IntegerField(
        verbose_name='Цена',
        default=0,
        editable=True,
        blank=True
    )

    class Meta:
        app_label = 'django_app'
        ordering = ('id',)
        verbose_name = 'Ice Cream'
        verbose_name_plural = 'Ice creams'


class Human(models.Model):
    firstname = models.CharField(
        verbose_name='Имя',
        default='',
        editable=True,
        max_length=100

    )
    surname = models.CharField(
        verbose_name='Фамилия',
        default='',
        editable=True,
        max_length=100

    )

    age = models.IntegerField(
        verbose_name='Возраст',
        default=0,
        editable=True,
        blank=True
    )

    salary = models.IntegerField(
        verbose_name='Зарплата',
        default=0,
        editable=True,
        blank=True
    )

    class Meta:
        app_label = 'django_app'
        ordering = ('id',)
        verbose_name = 'Человек'
        verbose_name_plural = 'Человечки'


class Child_model(models.Model):
    firstname = models.CharField(
        verbose_name='Имя',
        default='',
        editable=True,
        max_length=100

    )
    surname = models.CharField(
        verbose_name='Фамилия',
        default='',
        editable=True,
        max_length=100

    )

    age = models.IntegerField(
        verbose_name='Возраст',
        default=0,
        editable=True,
        blank=True
    )

    class Meta:
        app_label = 'django_app'
        ordering = ('id',)
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'

class Kiosk(models.Model):
    name = models.CharField(
        verbose_name='название',
        default='',
        editable=True,
        max_length=100

    )
    location = models.CharField(
        verbose_name='Местоположение',
        default='',
        editable=True,
        max_length=100

    )

    rating = models.IntegerField(
        verbose_name='рейтинг',
        default=0,
        editable=True,
        blank=True
    )

    salary = models.IntegerField(
        verbose_name='Прибыль',
        default=0,
        editable=True,
        blank=True
    )

    class Meta:
        app_label = 'django_app'
        ordering = ('id',)
        verbose_name = 'Kiosk'
        verbose_name_plural = 'Kiosks'