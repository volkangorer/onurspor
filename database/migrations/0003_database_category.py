# Generated by Django 2.0.3 on 2019-05-03 11:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_database_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='database',
            name='category',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Kategori'),
            preserve_default=False,
        ),
    ]
