# Generated by Django 2.1.2 on 2018-10-30 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0029_carouselitem_is_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselitem',
            name='is_photo',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]