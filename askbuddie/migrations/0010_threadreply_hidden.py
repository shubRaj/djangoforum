# Generated by Django 3.1.2 on 2021-02-13 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askbuddie', '0009_threadreply_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='threadreply',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
