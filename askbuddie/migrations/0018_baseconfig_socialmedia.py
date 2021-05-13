# Generated by Django 3.1.2 on 2021-02-13 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('askbuddie', '0017_auto_20210213_0611'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=12)),
                ('baseConfig', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='baseSocial', to='askbuddie.baseconfig')),
            ],
        ),
    ]
