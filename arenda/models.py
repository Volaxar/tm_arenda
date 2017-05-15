import os

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from sorl.thumbnail import ImageField, delete

from tmarenda.settings import UPLOAD_PHOTO_URL


class Kind(models.Model):
    kind = models.CharField(verbose_name='Название', max_length=30, help_text='Название типа')
    kind_plural = models.CharField(verbose_name='Название во мн. ч.', max_length=30,
                                   help_text='Название типа во множественном числе')

    image = models.ImageField(verbose_name='Неактивная иконка', upload_to='images/', default='')
    image_active = models.ImageField(verbose_name='Активная иконка', upload_to='images/', default='')

    class Meta:
        verbose_name = 'Тип помещения'
        verbose_name_plural = 'Типы помещений'
        ordering = ['id']

    def __str__(self):
        return self.kind


class Place(models.Model):
    """
    Помещение выставляемое для аренды
    """
    name = models.CharField(verbose_name='Название', max_length=100, help_text='Название помещения')
    area = models.FloatField(verbose_name='Площадь', help_text='Площадь помещения')
    floor = models.PositiveSmallIntegerField(verbose_name='Этаж', help_text='Этаж на котором расположено помещение')
    price = models.FloatField(verbose_name='Цена за кв.м', help_text='Цена за квадратный метр')
    desc = models.TextField(verbose_name='Описание', help_text='Подробное описание', blank=True)
    active = models.BooleanField(verbose_name='Показывать', help_text='Показывать помещение в списке', default=True)
    kinds = models.ManyToManyField(Kind, verbose_name='Типы помещений')

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'

    def __str__(self):
        return self.name


def get_file_path(instance, filename):
    """
    Функция генерирует путь для хранения фотографии помещения.

    :param instance: экземпляр модели помещения
    :param filename: имя файла
    :return: путь для сохранения фотографии, вида: UPLOAD_PHOTO_URL/ид_помещения/имя_файла
    """

    return os.path.join(UPLOAD_PHOTO_URL, str(instance.place.id), filename.lower())


class Image(models.Model):
    """
    Фотографии помещения
    """

    place = models.ForeignKey(Place, models.CASCADE)
    image = ImageField(verbose_name='Файл', upload_to=get_file_path)
    
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.image.name


@receiver(post_delete, sender=Image)
def image_file_delete(**kwargs):
    instance = kwargs['instance']

    storage, path = instance.image.storage, instance.image.path

    storage.delete(path)  # удаляем файл фото
    delete(instance.image)  # удаляем файл превью
