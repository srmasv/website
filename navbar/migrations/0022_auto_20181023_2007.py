# Generated by Django 2.1.2 on 2018-10-23 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0021_auto_20181023_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='hometext',
            name='body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hometext',
            name='header',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carouselitem',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='carouselitem',
            name='title',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]