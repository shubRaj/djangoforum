# Generated by Django 3.1.2 on 2021-02-17 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('askbuddie', '0036_auto_20210217_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threadreply',
            name='forumThread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thread_reply', related_query_name='withThreadReply', to='askbuddie.forumthread'),
        ),
    ]
