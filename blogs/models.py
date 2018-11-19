from django.db import models
from s3direct.fields import S3DirectField
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    heading = models.CharField(max_length=255)
    body = models.TextField()
    photo = S3DirectField(dest='blog')
    pub_date = models.DateTimeField(auto_now=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def short_text(self):
        if(len(self.body)<40):
            return self.body
        pos = self.body.rfind(' ',0,40)
        return self.body[:pos]+'...'

    def __str__(self):
        return self.heading
