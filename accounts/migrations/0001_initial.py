# Generated by Django 4.0.3 on 2022-04-18 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('celebrities', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=63, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRoutine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=31)),
                ('time', models.CharField(max_length=7)),
                ('is_completed', models.BooleanField(default=False)),
                ('celebrity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='celebrities.celebrity')),
                ('imitated_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]
