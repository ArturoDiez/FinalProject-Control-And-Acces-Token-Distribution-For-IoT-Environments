# Generated by Django 3.0.3 on 2020-05-28 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServicioIoT', '0017_auto_20200525_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extradata',
            name='expires_in',
        ),
        migrations.RemoveField(
            model_name='extradata',
            name='token_update_time',
        ),
    ]
