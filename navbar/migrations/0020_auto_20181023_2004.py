# Generated by Django 2.1.2 on 2018-10-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0019_auto_20181023_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hometext',
            name='body',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='hometext',
            name='header',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]