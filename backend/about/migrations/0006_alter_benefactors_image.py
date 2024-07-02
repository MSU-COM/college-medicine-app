# Generated by Django 5.0.6 on 2024-07-02 07:21

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_alter_benefactors_name_alter_benefactors_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benefactors',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='default.png', force_format=None, keep_meta=True, null=True, quality=85, scale=None, size=[400, 400], upload_to='benefactors'),
        ),
    ]
