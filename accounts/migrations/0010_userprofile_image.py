# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to=b'profile_image'),
        ),
    ]
