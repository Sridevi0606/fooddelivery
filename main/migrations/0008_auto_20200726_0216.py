# Generated by Django 3.0.4 on 2020-07-25 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200725_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='instructions',
            field=models.CharField(default='Medium Spicy/Non-Jain', max_length=200),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
