# Generated by Django 3.0.4 on 2020-07-25 21:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_cartitems_ordered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='ordered_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
