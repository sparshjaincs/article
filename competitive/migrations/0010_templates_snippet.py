# Generated by Django 3.0.8 on 2020-12-23 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitive', '0009_templates_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='templates',
            name='snippet',
            field=models.TextField(blank=True),
        ),
    ]
