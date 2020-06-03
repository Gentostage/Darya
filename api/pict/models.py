# Create your models here.
from PIL import Image
from django.db import models
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust, ResizeToFill


class Works(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"Название")
    descriptions = models.TextField(max_length=500, verbose_name=u"Описание")
    mainPic = models.ImageField(upload_to='mPic', height_field=None, width_field=None, max_length=100,
                                verbose_name=u"Главная картинка", default='default-image.jpg')

    mainCompressPic = ImageSpecField(source='mainPic',
                          format='JPEG',
                          options={'quality': 90},
                          processors=[Adjust(contrast=1.2, sharpness=1.1),
                                      ResizeToFill(389, 380)])

    webMainCompressPic = ImageSpecField(source='mainPic',
                            format='WEBP',
                            options={'quality': 90},
                            processors=[Adjust(contrast=1.2, sharpness=1.1),
                                        ResizeToFill(389, 380)])

    class Meta:
        verbose_name = u"Работа"
        verbose_name_plural = u"Работы"

    def __str__(self):
        return self.name


class Pictures(models.Model):
    work = models.ForeignKey(Works, related_name='picture', on_delete=models.CASCADE, verbose_name=u"Картинкы")

    pic = models.ImageField(upload_to='pic', height_field=None, width_field=None, max_length=100
                            , verbose_name=u"Картинка")

    compressPic = ImageSpecField(source='pic',
                                 format='JPEG',
                                 options={'quality': 90},
                                 processors=[Adjust(contrast=1.2, sharpness=1.1),
                                             ResizeToFit(1000, 1000)])

    mobileCompressPic = ImageSpecField(source='pic',
                          format='JPEG',
                          options={'quality': 90},
                          processors=[Adjust(contrast=1.2, sharpness=1.1),
                                      ResizeToFit(600, 600)])

    webPic = ImageSpecField(source='pic',
                            format='WEBP',
                            options={'quality': 90},
                            processors=[Adjust(contrast=1.2, sharpness=1.1),
                                        ResizeToFit(1000, 1000)])

    mobileWebPic = ImageSpecField(source='pic',
                             format='WEBP',
                             options={'quality': 90},
                             processors=[Adjust(contrast=1.2, sharpness=1.1),
                                         ResizeToFit(600, 600)])

    class Meta:
        verbose_name = u"Картина"
        verbose_name_plural = u"Картины"
