# Generated by Django 2.2.3 on 2020-03-12 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='dateandtime',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=models.SlugField(),
        ),
    ]
