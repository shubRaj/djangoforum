# Generated by Django 3.1.2 on 2021-02-20 13:14

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askbuddie', '0047_auto_20210220_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basepage',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]