# Generated by Django 3.0.4 on 2020-07-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_cartitems_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Delivered', 'Delivered')], default='Active', max_length=20),
        ),
    ]
