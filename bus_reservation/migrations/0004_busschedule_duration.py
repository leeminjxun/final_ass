# Generated by Django 5.1.3 on 2024-11-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_reservation', '0003_busschedule_alter_reservation_seatnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='busschedule',
            name='duration',
            field=models.DurationField(default=None, null=True),
        ),
    ]
