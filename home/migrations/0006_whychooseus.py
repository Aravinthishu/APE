# Generated by Django 5.1.4 on 2025-01-20 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_clientlogo_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhyChooseUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='whychooseus/')),
            ],
        ),
    ]
