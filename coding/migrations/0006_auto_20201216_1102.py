# Generated by Django 3.0.8 on 2020-12-16 05:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0005_auto_20201215_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 16, 11, 2, 54, 441769)),
        ),
        migrations.AlterField(
            model_name='anwsers',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 16, 11, 2, 54, 433771)),
        ),
        migrations.AlterField(
            model_name='aptitude',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 16, 11, 2, 54, 441769)),
        ),
        migrations.AlterField(
            model_name='articles',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 16, 11, 2, 54, 424510)),
        ),
        migrations.AlterField(
            model_name='list',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 16, 11, 2, 54, 441769)),
        ),
    ]
