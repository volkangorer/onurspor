# Generated by Django 2.0.3 on 2019-05-20 20:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_auto_20190520_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duyuru',
            name='duyuru_content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
