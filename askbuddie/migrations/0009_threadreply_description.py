# Generated by Django 3.1.2 on 2021-02-13 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askbuddie', '0008_auto_20210212_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='threadreply',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]