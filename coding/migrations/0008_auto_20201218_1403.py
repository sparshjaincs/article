# Generated by Django 3.0.8 on 2020-12-18 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0007_auto_20201217_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 18, 14, 3, 53, 914821)),
        ),
        migrations.AlterField(
            model_name='anwsers',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 18, 14, 3, 53, 906826)),
        ),
        migrations.AlterField(
            model_name='aptitude',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 18, 14, 3, 53, 914821)),
        ),
        migrations.AlterField(
            model_name='articles',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 18, 14, 3, 53, 898836)),
        ),
        migrations.AlterField(
            model_name='list',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 18, 14, 3, 53, 914821)),
        ),
    ]
