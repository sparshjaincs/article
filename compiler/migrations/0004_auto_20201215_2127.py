# Generated by Django 3.0.8 on 2020-12-15 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compiler', '0003_auto_20201215_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playground',
            name='code',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
