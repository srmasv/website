from django.db import models
from django.forms import ValidationError

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
    title = models.CharField(max_length=40)
    subtitle = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Carousel Item"
        verbose_name_plural = "Carousel Items"

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
