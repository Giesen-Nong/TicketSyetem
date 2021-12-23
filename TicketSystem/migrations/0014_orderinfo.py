# Generated by Django 3.2.10 on 2021-12-23 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketSystem', '0013_order_seat'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderinfo',
            fields=[
                ('O_Id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('seat', models.IntegerField()),
                ('u_id', models.CharField(max_length=18)),
                ('f_id', models.CharField(max_length=20)),
                ('s_time', models.DateTimeField()),
                ('a_time', models.DateTimeField()),
                ('origin', models.CharField(max_length=20)),
                ('des', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=10)),
                ('status', models.BooleanField()),
            ],
            options={
                'db_table': 'order_view',
                'managed': False,
            },
        ),
    ]