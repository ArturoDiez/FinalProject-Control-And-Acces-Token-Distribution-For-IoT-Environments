# Generated by Django 3.0.3 on 2020-02-23 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServicioIoT', '0009_auto_20200223_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
