# Generated by Django 2.2.4 on 2019-08-21 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0010_post_pinned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=5000),
        ),
    ]