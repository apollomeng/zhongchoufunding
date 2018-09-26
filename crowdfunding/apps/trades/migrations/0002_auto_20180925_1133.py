# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-25 11:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operations', '0002_auto_20180925_1133'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trades', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersupport',
            name='support_man',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='支持人'),
        ),
        migrations.AddField(
            model_name='usersupport',
            name='support_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Projects', verbose_name='支持项目'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operations.UserAddress', verbose_name='用户地址'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='support_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.SupportItems', verbose_name='支持的回报项目'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
