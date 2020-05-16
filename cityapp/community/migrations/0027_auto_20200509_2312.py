# Generated by Django 2.2.7 on 2020-05-09 23:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0026_auto_20200503_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_text',
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_post', to='community.Post'),
        ),
    ]