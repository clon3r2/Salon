# Generated by Django 4.0.2 on 2022-02-08 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0002_service_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
