# Generated by Django 2.2.4 on 2019-08-19 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]