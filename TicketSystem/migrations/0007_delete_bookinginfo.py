# Generated by Django 3.2.10 on 2021-12-21 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TicketSystem', '0006_delete_travelagency'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookingInfo',
        ),
    ]