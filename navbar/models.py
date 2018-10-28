from django.db import models
from django.forms import ValidationError

from django.conf import settings
from PIL import Image
import os, platform

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
    item = models.FileField(upload_to="carousel/", help_text="This image/video will always take some time to process for each save. Please be patient.")
    is_photo = models.BooleanField(default=True)
    extension = models.CharField(max_length=4, help_text="You need to assign the value yourself.")

    class Meta:
        verbose_name = "Carousel Item"
        verbose_name_plural = "Carousel Items"

    def save(self, *args, **kwargs):
        super(CarouselItem, self).save(*args, **kwargs)
        filename = str(self.item.file)
        try:
            image = Image.open(filename, "r")
            new_image = image.resize((800, 400))
            new_image.save(filename)
            self.is_photo = True

        except OSError:
            #Not an Image
            if platform.system()=="Darwin":
                ffmpeg = os.path.join(settings.BASE_DIR, "ffmpeg-osx")
            elif platform.system()=="Linux":
                ffmpeg = os.path.join(settings.BASE_DIR, "ffpmeg-linux")
            else:
                return
            os.system(ffmpeg + ' -i %s -vf "scale=800:400:force_original_aspect_ratio=decrease,pad=800:400:(ow-iw)/2:(oh-ih)/2" %s1%s' % (filename, filename[:-4], filename[-4:]))
            os.remove("%s" % filename)
            os.rename("%s1%s" % (filename[:-4], filename[-4:]), "%s" % filename)
            self.is_photo = False

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
