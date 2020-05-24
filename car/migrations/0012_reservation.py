# Generated by Django 3.0.4 on 2020-05-23 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0011_auto_20200519_0056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('checkin', models.DateField()),
                ('checkout', models.DateField()),
                ('days', models.IntegerField(default='1')),
                ('total', models.FloatField()),
                ('status', models.CharField(choices=[('New', 'Yeni'), ('Accepted', 'Onaylandı'), ('Canceled', 'Reddedildi')], default='New', max_length=10)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('message', models.CharField(blank=True, max_length=255)),
                ('note', models.CharField(blank=True, max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.Car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
