# Generated by Django 3.1.2 on 2021-02-13 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askbuddie', '0014_auto_20210213_0451'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forumthread',
            options={},
        ),
        migrations.AlterModelOptions(
            name='threadreply',
            options={},
        ),
        migrations.AlterField(
            model_name='forumthread',
            name='views',
            field=models.IntegerField(default=1),
        ),
    ]
