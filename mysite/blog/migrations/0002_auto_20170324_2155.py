# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 18:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publish_date',
            new_name='published_date',
        ),
    ]
