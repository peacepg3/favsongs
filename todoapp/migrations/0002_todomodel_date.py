# Generated by Django 4.0.2 on 2022-03-11 05:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='date',
            field=models.DateField(default=datetime.date(2022, 3, 11)),
        ),
    ]
