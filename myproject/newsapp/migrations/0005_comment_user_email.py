# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-13 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0004_auto_20171212_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_email',
            field=models.TextField(blank=True, null=True),
        ),
    ]