# Generated by Django 3.2.8 on 2021-11-10 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_orders_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='amount',
        ),
    ]
