# Generated by Django 5.1.1 on 2024-09-10 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingCar', '0004_places_dateedit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='PlaceCodeQr',
            field=models.CharField(default='N/A', max_length=500),
        ),
        migrations.AlterField(
            model_name='places',
            name='PlaceCodeQr',
            field=models.CharField(default='N/A', max_length=500),
        ),
    ]
