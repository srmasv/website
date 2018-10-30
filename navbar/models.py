from django.db import models
from django.forms import ValidationError

from django.conf import settings
from PIL import Image
import os, subprocess

# Create your models here.
class NavItem(models.Model):
    text = models.CharField(max_length=10)
    url_name = models.CharField(max_length=40)
    position = models.IntegerField(default=0, unique=True)

    class Meta:
        verbose_name = "Navbar Item"
        verbose_name_plural = "Navbar Items"

    def __str__(self):
        return self.text

class HomeText(models.Model):
    header = models.CharField(max_length=255)
    body = models.TextField()
    subtitle = models.TextField()

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = "Home Top Text"
        verbose_name_plural = verbose_name

    def clean(self):
        if HomeText.objects.exists() and not self.pk:
            raise ValidationError("Only one instance of HomeText can be made.")

class CarouselItem(models.Model):
    title = models.CharField(max_length=40, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    item = models.FileField(upload_to="carousel/", help_text="If you are uploading a photo, it must be a png or jpg. If you are uploading a video, it must be 800x400 and in mp4 format.")
    is_photo = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return str(os.path.basename(self.item.name))

    class Meta:
        verbose_name = "Carousel Item"
        verbose_name_plural = "Carousel Items"

    def save(self, *args, **kwargs):
        self.is_photo = os.path.splitext(self.item.name)[1] in [".jpg", ".png", ".jpeg"]
        super(CarouselItem, self).save(*args, **kwargs)
        filename = str(self.item.file)
        if os.path.splitext(filename)[1] in [".jpg", ".png", ".jpeg"]:
            image = Image.open(filename, "r")
            new_image = image.resize((800, 400))
            new_image.save(filename)
        elif os.path.splitext(filename)[1]==".mp4":
            size = subprocess.check_output(os.path.join(settings.BASE_DIR, "ffprobe") + " -v error -select_streams v:0 -show_entries\
             stream=width,height -of csv=p=0 %s" % filename, shell=True).decode().strip().split(",")
            if size!=["800","400"]:
                self.delete()
                raise ValidationError("The video is not 800x400 in size. Upload some other video.")


class JourneyText(models.Model):
    heading = models.CharField(max_length=20)
    title =  models.CharField(max_length=40)
    body = models.TextField()
    image = models.ImageField(upload_to="images/")
    btn_text = models.CharField(max_length=10)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = "Journey Text"
        verbose_name_plural = verbose_name

    def clean(self):
        if JourneyText.objects.exists() and not self.pk:
            raise ValidationError("Only one instance of HomeText can be made.")

class DomainText(models.Model):
    icon = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    body = models.TextField()
    position = models.IntegerField(default=0,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Domain Info"
        verbose_name_plural = "Domain Infos"
