# Generated by Django 3.0.4 on 2020-08-24 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0018_item_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rslug', models.SlugField(default='sushi-slug')),
                ('review', models.TextField()),
                ('posted_on', models.DateField(default=django.utils.timezone.now)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
