# Generated by Django 2.2.3 on 2020-03-18 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0002_auto_20200312_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='categorySlug',
            field=models.SlugField(default=''),
        ),
    ]
