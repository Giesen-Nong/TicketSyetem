# Generated by Django 3.2.10 on 2021-12-21 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketSystem', '0003_remove_userinfo_u_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='U_password',
            field=models.CharField(default='123456', max_length=30),
        ),
    ]
