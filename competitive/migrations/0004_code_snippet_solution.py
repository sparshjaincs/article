# Generated by Django 3.0.8 on 2020-12-22 05:36

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compiler', '0005_auto_20201216_1102'),
        ('competitive', '0003_programming_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, unique=True)),
                ('solution', ckeditor.fields.RichTextField(blank=True)),
                ('video', models.TextField(blank=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_sol', to='competitive.Programming', to_field='title')),
            ],
        ),
        migrations.CreateModel(
            name='Code_Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', ckeditor.fields.RichTextField(blank=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='language_name', to='compiler.Language', to_field='lang')),
                ('solution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sol_Snippet', to='competitive.Solution', to_field='title')),
            ],
        ),
    ]
