# Generated by Django 3.0.8 on 2020-12-22 03:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0012_auto_20201222_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 22, 9, 20, 53, 762707)),
        ),
        migrations.AlterField(
            model_name='anwsers',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 22, 9, 20, 53, 754712)),
        ),
        migrations.AlterField(
            model_name='aptitude',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 22, 9, 20, 53, 770704)),
        ),
        migrations.AlterField(
            model_name='articles',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 22, 9, 20, 53, 746714)),
        ),
        migrations.AlterField(
            model_name='list',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 22, 9, 20, 53, 770704)),
        ),
    ]
