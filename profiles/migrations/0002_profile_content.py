# Generated by Django 3.2.23 on 2023-11-26 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
