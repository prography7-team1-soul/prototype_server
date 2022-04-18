# Generated by Django 4.0.3 on 2022-04-18 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0004_celebrity_children'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelebrityTmi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=31)),
            ],
        ),
        migrations.RemoveField(
            model_name='celebrity',
            name='tmi',
        ),
        migrations.AddField(
            model_name='celebrity',
            name='tmi',
            field=models.ManyToManyField(to='celebrities.celebritytmi'),
        ),
    ]
