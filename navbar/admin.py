from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.NavItem)
admin.site.register(models.HomeText)
admin.site.register(models.CarouselItem)
admin.site.register(models.JourneyText)
