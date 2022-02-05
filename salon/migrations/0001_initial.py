# Generated by Django 3.2 on 2022-02-05 17:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Full Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('profile_pic', models.FileField(blank=True, default=None, null=True, upload_to='agent images/', verbose_name='Agent Picture')),
                ('service_reach', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Service Number Reach')),
                ('experience_year', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Years Of Experience')),
            ],
        ),
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(6, 'شنبه'), (0, 'یکشنبه'), (1, 'دوشنبه'), (2, 'سه شنبه'), (3, 'چهارشنبه'), (4, 'پنجشنبه'), (5, 'جمعه')], unique=True)),
                ('is_weekend', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Service Field')),
                ('duration', models.DurationField(blank=True, default=datetime.timedelta(seconds=3600), null=True, verbose_name='Service Timespan')),
                ('adultPrice', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('childPrice', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child', models.IntegerField(blank=True, default=0, null=True)),
                ('adult', models.IntegerField(blank=True, default=0, null=True)),
                ('reservedDate', models.DateField()),
                ('reservedTime', models.CharField(max_length=200)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.agent')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.customer')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.service')),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.service'),
        ),
    ]