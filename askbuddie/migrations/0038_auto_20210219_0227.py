# Generated by Django 3.1.2 on 2021-02-19 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askbuddie', '0037_auto_20210217_1414'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='threadreply',
            options={'ordering': ('-upvotes', '-hearts', '-created_on'), 'verbose_name_plural': 'ThreadReplies'},
        ),
    ]
