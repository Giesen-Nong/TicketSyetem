# Generated by Django 3.2.10 on 2021-12-23 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketSystem', '0009_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightinfo',
            name='num',
            field=models.IntegerField(default=150),
        ),
        migrations.AddField(
            model_name='flightinfo',
            name='num_c',
            field=models.IntegerField(default=0),
        ),
    ]
