# Generated by Django 5.1.4 on 2025-01-31 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_whatwedo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('position', models.CharField(blank=True, max_length=200, null=True)),
                ('testimonial', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='testimonial/')),
            ],
        ),
    ]
