# Generated by Django 4.0.3 on 2022-04-06 09:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celebrity',
            name='routines',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=8),
        ),
    ]
