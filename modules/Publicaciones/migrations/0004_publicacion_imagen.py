# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-14 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publicaciones', '0003_auto_20170211_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='Publicaciones/'),
        ),
    ]
