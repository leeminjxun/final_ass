# Generated by Django 5.1.3 on 2024-11-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_reservation', '0005_alter_busschedule_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busschedule',
            name='duration',
            field=models.DurationField(default=None, null=True),
        ),
    ]
