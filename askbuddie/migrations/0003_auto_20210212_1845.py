# Generated by Django 3.1.2 on 2021-02-12 18:45

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('askbuddie', '0002_auto_20210212_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumthread',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='forumthread',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='forumthread',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='forumthread',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('arts', 'Arts'), ('edu', 'Education'), ('entertain', 'Entertainment'), ('gam', 'Gaming'), ('hobbies', 'Hobbies'), ('pets', 'Pets'), ('photo', 'Photography'), ('politics', 'Politics'), ('rand', 'Random'), ('sci', 'Science'), ('social', 'Social'), ('tech', 'Tech'), ('travel', 'Travel'), ('vid', 'Video')], max_length=12, null=True),
        ),
    ]
