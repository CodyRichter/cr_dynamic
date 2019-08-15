# Generated by Django 2.2.4 on 2019-08-15 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=500)),
                ('image_link', models.CharField(max_length=256)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]