# Generated by Django 2.2.7 on 2019-11-12 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_auto_20191111_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataCharField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=55)),
                ('char_field', models.CharField(max_length=55)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DataFloatField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=55)),
                ('float_field', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DataImageField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=55)),
                ('image_field', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DataLocationField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=55)),
                ('location_lon_field', models.FloatField()),
                ('location_lat_field', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DataTextField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=55)),
                ('text_field', models.TextField(max_length=55)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostDataType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('data_char_field', models.ManyToManyField(blank=True, to='community.DataCharField')),
                ('data_float_field', models.ManyToManyField(blank=True, to='community.DataFloatField')),
                ('data_image_field', models.ManyToManyField(blank=True, to='community.DataImageField')),
                ('data_location_field', models.ManyToManyField(blank=True, to='community.DataLocationField')),
                ('data_text_field', models.ManyToManyField(blank=True, to='community.DataTextField')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='post',
            name='data_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='community.PostDataType'),
        ),
    ]