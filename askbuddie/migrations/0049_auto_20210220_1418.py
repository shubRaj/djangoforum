# Generated by Django 3.1.2 on 2021-02-20 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askbuddie', '0048_auto_20210220_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumthread',
            name='image',
        ),
        migrations.RemoveField(
            model_name='threadreply',
            name='image',
        ),
    ]
