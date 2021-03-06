# Generated by Django 3.0.4 on 2020-04-03 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_name', models.CharField(max_length=50)),
                ('my_description', models.TextField()),
                ('languages_learnt', models.FilePathField(path='homepage/static/img')),
                ('my_image', models.FilePathField(path='homepage/static/img')),
                ('my_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
