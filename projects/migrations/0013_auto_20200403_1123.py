# Generated by Django 3.0.4 on 2020-04-03 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20200403_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='projects/static/img'),
        ),
    ]
