# Generated by Django 3.0.4 on 2020-07-27 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_cartitems_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='status',
        ),
    ]
