# Generated by Django 3.1.2 on 2021-02-26 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askbuddie', '0056_threadtag_forumthread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basepage',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='forumthread',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='threadreply',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
