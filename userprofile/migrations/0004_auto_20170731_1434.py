# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20170731_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]