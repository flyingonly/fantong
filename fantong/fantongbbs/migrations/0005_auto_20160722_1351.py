# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 05:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fantongbbs', '0004_auto_20160722_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbspost',
            name='PUserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
