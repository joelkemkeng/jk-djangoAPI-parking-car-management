# Generated by Django 5.1.1 on 2024-09-10 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkingCar', '0007_history_time_places_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Departement',
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
    ]
