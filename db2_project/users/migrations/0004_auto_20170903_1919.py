# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-03 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170901_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
