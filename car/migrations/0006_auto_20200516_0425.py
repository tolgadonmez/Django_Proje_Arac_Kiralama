# Generated by Django 3.0.4 on 2020-05-16 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_auto_20200516_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='slug',
            field=models.SlugField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='car',
            name='keywords',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='car',
            name='marka',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='title',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='keywords',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
