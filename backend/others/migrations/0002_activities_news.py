# Generated by Django 5.0.6 on 2024-06-10 11:19

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('date_held', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
                'ordering': ['-date_held'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, default='default.png', null=True, upload_to='news')),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'ordering': ['-date_added'],
            },
        ),
    ]
