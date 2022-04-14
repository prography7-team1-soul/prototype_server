# Generated by Django 4.0.3 on 2022-04-14 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CelebrityJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('background_color', models.CharField(choices=[('soulMain', 'Main'), ('soulSub', 'Sub'), ('soulBlack', 'Black'), ('soulGray1', 'Gray1'), ('soulGray2', 'Gray2'), ('soulRed1', 'Red1'), ('soulRed2', 'Red2'), ('soulNegative', 'Negative'), ('soulGreen1', 'Green1'), ('soulGreen2', 'Green2'), ('soulPink1', 'Pink1'), ('soulPink2', 'Pink2')], max_length=31)),
                ('text_color', models.CharField(choices=[('soulMain', 'Main'), ('soulSub', 'Sub'), ('soulBlack', 'Black'), ('soulGray1', 'Gray1'), ('soulGray2', 'Gray2'), ('soulRed1', 'Red1'), ('soulRed2', 'Red2'), ('soulNegative', 'Negative'), ('soulGreen1', 'Green1'), ('soulGreen2', 'Green2'), ('soulPink1', 'Pink1'), ('soulPink2', 'Pink2')], max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('english_name', models.CharField(max_length=31)),
                ('image', models.ImageField(upload_to='')),
                ('MBTI', models.CharField(max_length=7)),
                ('nationality', models.CharField(max_length=15)),
                ('introduction', models.TextField()),
                ('body_spec', models.JSONField()),
                ('education', models.CharField(max_length=63)),
                ('wise_saying', models.JSONField()),
                ('wealth', models.CharField(max_length=63)),
                ('spouse', models.CharField(max_length=31)),
                ('children', models.CharField(max_length=63)),
                ('age', models.PositiveIntegerField()),
                ('birthday', models.CharField(max_length=31)),
                ('deceased_at', models.CharField(max_length=31)),
                ('celebrity_routines', models.JSONField()),
                ('tmi', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='celebrities.celebrityjob')),
            ],
        ),
    ]
