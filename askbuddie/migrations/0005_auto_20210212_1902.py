# Generated by Django 3.1.2 on 2021-02-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askbuddie', '0004_auto_20210212_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='threadreply',
            name='views',
        ),
        migrations.AddField(
            model_name='threadreply',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]