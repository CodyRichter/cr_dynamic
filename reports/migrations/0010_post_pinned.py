# Generated by Django 2.2.4 on 2019-08-21 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_auto_20190820_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]
