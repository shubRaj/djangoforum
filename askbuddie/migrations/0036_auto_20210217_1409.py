# Generated by Django 3.1.2 on 2021-02-17 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('askbuddie', '0035_auto_20210217_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threadreply',
            name='forumThread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thread_reply', to='askbuddie.forumthread'),
        ),
    ]
