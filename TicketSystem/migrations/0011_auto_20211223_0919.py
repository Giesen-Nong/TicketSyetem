# Generated by Django 3.2.10 on 2021-12-23 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketSystem', '0010_auto_20211223_0914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightinfo',
            name='num_c',
        ),
        migrations.AddField(
            model_name='flightinfo',
            name='num_a',
            field=models.IntegerField(default=150),
        ),
    ]