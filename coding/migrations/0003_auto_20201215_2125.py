# Generated by Django 3.0.8 on 2020-12-15 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0002_auto_20201215_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 15, 21, 25, 58, 339531)),
        ),
        migrations.AlterField(
            model_name='anwsers',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 15, 21, 25, 58, 339531)),
        ),
        migrations.AlterField(
            model_name='aptitude',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 15, 21, 25, 58, 339531)),
        ),
        migrations.AlterField(
            model_name='articles',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 15, 21, 25, 58, 323880)),
        ),
        migrations.AlterField(
            model_name='list',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 15, 21, 25, 58, 339531)),
        ),
    ]
