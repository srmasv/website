from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.NavItem)
admin.site.register(models.HomeText)
admin.site.register(models.CarouselItem)
admin.site.register(models.JourneyText)
admin.site.register(models.DomainText)
admin.site.register(models.Recent)
admin.site.register(models.Objective)
admin.site.register(models.ObjectiveText)
admin.site.register(models.Logo)
