# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 04:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0004_auto_20171110_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='user_type',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cmdb.UserType'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_type_id',
            field=models.IntegerField(choices=[(1, '超级用户'), (2, '普通用户')], default=1),
        ),
    ]