# Generated by Django 5.1.4 on 2025-01-18 08:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('citizen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FIR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('photos_or_videos', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('citizen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='firs', to='citizen.citizen')),
            ],
        ),
    ]
