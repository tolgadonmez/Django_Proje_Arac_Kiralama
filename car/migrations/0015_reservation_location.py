# Generated by Django 3.0.4 on 2020-05-24 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0014_auto_20200524_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='location',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]