# Generated by Django 3.0.4 on 2020-05-15 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.Car')),
            ],
        ),
    ]
