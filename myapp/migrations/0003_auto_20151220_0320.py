# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-19 23:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='question',
        ),
    ]