# Generated by Django 3.0.8 on 2020-11-24 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_remove_note_desciption'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-created']},
        ),
    ]
