# Generated by Django 3.0.8 on 2020-12-15 15:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compiler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='template',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='playground',
            name='title',
            field=models.CharField(default='Untitled', max_length=1000),
        ),
    ]
