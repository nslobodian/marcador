# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-25 16:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marcador', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PublicBookmarkManager',
        ),
    ]
