# Generated by Django 3.0.4 on 2020-04-20 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200420_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FilePathField(default='', path='blog/static/img'),
        ),
    ]
