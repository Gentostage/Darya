# Create your models here.
from django.db import models


class Works(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"Название")
    descriptions = models.TextField(max_length=500, verbose_name=u"Описание")

    class Meta:
        verbose_name = u"Работа"
        verbose_name_plural = u"Работы"

    def __str__(self):
        return self.name


class Pictures(models.Model):
    work = models.ForeignKey(Works, related_name='picture', on_delete='CASCADE', verbose_name=u"Картинкы")
    pic = models.ImageField(upload_to='pic', height_field=None, width_field=None, max_length=100,
                            verbose_name=u"Картинка")

    class Meta:
        verbose_name = u"Картина"
        verbose_name_plural = u"Картины"
