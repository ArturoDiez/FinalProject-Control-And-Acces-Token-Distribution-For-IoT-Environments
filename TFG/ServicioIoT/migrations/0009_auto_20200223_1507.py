# Generated by Django 3.0.3 on 2020-02-23 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ServicioIoT', '0008_auto_20200223_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='grupo',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='nombregrupo', to='ServicioIoT.GrupoDispositivo'),
        ),
    ]