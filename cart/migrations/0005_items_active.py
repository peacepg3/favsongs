# Generated by Django 4.0.2 on 2022-05-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cartlist_items_delete_cart_items_delete_cart_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
