# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyNote', '0004_menusinfo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menusinfo',
            name='left_child',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='menusinfo',
            name='parentID',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='menusinfo',
            name='right_sibling',
            field=models.IntegerField(default=0),
        ),
    ]
