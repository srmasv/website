# Generated by Django 2.1.2 on 2018-10-30 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0031_auto_20181030_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselitem',
            name='item',
            field=models.CharField(help_text='File URL. For standards of this website, if you are uploading a photo/video, it must be 800x400 and in jpg,png,jpeg/mp4 format respectively. PLEASE FOLLOW THIS GUIDELINE VERY CAREFULLY.', max_length=255),
        ),
    ]