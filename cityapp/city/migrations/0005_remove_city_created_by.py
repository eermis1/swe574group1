# Generated by Django 2.2.7 on 2020-05-18 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0004_city_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='created_by',
        ),
    ]
