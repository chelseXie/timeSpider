# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=11)),
                ('openId', models.CharField(max_length=32)),
                ('nickName', models.CharField(max_length=32)),
                ('registerTime', models.CharField(max_length=19)),
                ('loginTime', models.CharField(max_length=19)),
                ('createTime', models.CharField(max_length=19)),
            ],
        ),
    ]