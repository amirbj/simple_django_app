# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 00:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20151225_2333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='password',
            new_name='password1',
        ),
    ]