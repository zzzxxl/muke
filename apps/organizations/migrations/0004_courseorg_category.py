# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-06 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_courseorg_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')], default='gx', max_length=20, verbose_name='机构类别'),
        ),
    ]
