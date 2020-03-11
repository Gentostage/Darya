from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Pictures, Works


class PicturesShotsInline(admin.TabularInline):
    model = Pictures
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe('<img src="%s" height="350">' % obj.pic.url)

    get_image.short_description = "Изображение"


@admin.register(Works)
class WorksAdmin(admin.ModelAdmin):
    save_as = True
    inlines = [PicturesShotsInline, ]
    readonly_fields = ("main_image", )

    def main_image(self, obj):
        return mark_safe(('<img src="%s" height="350">' % obj.mainPic.url))


@admin.register(Pictures)
class PicturesAdmin(admin.ModelAdmin):
    list_display = ("id", "pic")

    def pic(self, obj):
        return mark_safe('<img src="%s" width="400" height="400">' % obj.image)

    pic.short_description = "Изображение"
