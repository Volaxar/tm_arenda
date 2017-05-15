from django.contrib import admin

from arenda.models import Place, Image, Kind
from grid_images import GridImagesInline


class ImageInline(GridImagesInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fields = (('name', 'active'), 'floor', ('area', 'price'), 'desc', 'kinds')
    filter_horizontal = ('kinds',)
    list_display = ('name', 'floor', 'area', 'price', 'active')
    
    inlines = [
        ImageInline,
    ]


@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    pass


