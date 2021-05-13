# Generated by Django 3.1.2 on 2021-02-12 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('askbuddie', '0003_auto_20210212_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumthread',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_thread', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ThreadReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(default=0)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_reply', to=settings.AUTH_USER_MODEL)),
                ('forumThread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thread_reply', to='askbuddie.forumthread')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]