# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-05 17:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0011_share_job_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beinterested',
            old_name='be_interested_uuid',
            new_name='uuid',
        ),
        migrations.RenameField(
            model_name='share',
            old_name='share_uuid',
            new_name='uuid',
        ),
    ]
