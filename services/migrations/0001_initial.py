# Generated by Django 5.1.4 on 2025-01-29 12:43

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('long_desc', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='services/')),
            ],
        ),
    ]
