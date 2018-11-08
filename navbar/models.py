from django.db import models
from django.forms import ValidationError

from django.conf import settings
from PIL import Image
import os, subprocess
from s3direct.fields import S3DirectField

#To scale videos using ffmpeg
# ffmpeg -i input -vf "scale=w=1280:h=720:force_original_aspect_ratio=1,pad=1280:720:(ow-iw)/2:(oh-ih)/2" output


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
    item = S3DirectField(dest="carousel", help_text="For standards of this website, if you are uploading a photo/video, it must be 800x400 and in jpg,png,jpeg/mp4 format respectively. PLEASE FOLLOW THIS GUIDELINE VERY CAREFULLY.")
    is_photo = models.BooleanField(default=False, help_text="Please specify if this is a photo or not.")

    def __str__(self):
        return os.path.basename(self.item)

    class Meta:
        verbose_name = "Carousel Item"
        verbose_name_plural = "Carousel Items"

class JourneyText(models.Model):
    heading = models.CharField(max_length=20)
    title =  models.CharField(max_length=40)
    body = models.TextField()
    image = S3DirectField(dest="media")
    btn_text = models.CharField(max_length=10)

    def __str__(self):
        return os.path.basename(self.image)

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
