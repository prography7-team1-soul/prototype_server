# Generated by Django 4.0.3 on 2022-04-08 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0003_alter_celebrity_birthday_alter_celebrity_children_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='celebrity',
            name='english_name',
            field=models.CharField(default='Steve Jobs', max_length=31),
            preserve_default=False,
        ),
    ]
