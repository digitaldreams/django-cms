# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20171209_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, null=True, unique=True),
        ),
    ]
