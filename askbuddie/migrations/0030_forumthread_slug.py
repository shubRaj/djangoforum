# Generated by Django 3.1.2 on 2021-02-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askbuddie', '0029_baseconfig_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumthread',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
