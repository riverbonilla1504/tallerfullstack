# Generated by Django 5.2 on 2025-04-04 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("AppVehiculos", "0002_alter_vehiculo_color_alter_vehiculo_placa_customuser"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]
