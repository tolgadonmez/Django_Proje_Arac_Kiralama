# Generated by Django 3.0.4 on 2020-05-15 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200515_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='contact',
        ),
    ]