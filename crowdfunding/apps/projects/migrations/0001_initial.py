# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-25 11:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=200, upload_to='banners/%y/%m/%d', verbose_name='首页轮播图片')),
                ('index', models.IntegerField(default=1, verbose_name='图片顺序')),
                ('url', models.URLField(verbose_name='轮播链接')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '轮播信息',
                'verbose_name_plural': '轮播信息',
            },
        ),
        migrations.CreateModel(
            name='IndexCategoryAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=1, verbose_name='广告项目顺序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '首页广告项目',
                'verbose_name_plural': '首页广告项目',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='项目名称')),
                ('title_image', models.ImageField(max_length=200, upload_to='projects/%y/%m/%d', verbose_name='项目头图')),
                ('target_funding', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='筹资金额')),
                ('support_funding', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='支持金额')),
                ('status', models.CharField(choices=[('即将开始', '即将开始'), ('众筹中', '众筹中'), ('众筹成功', '众筹成功')], default='即将开始', max_length=20, verbose_name='项目状态')),
                ('due_days', models.IntegerField(default=0, verbose_name='筹资天数')),
                ('desc', models.TextField(blank=True, max_length=100, null=True, verbose_name='项目简介')),
                ('detail', models.TextField(blank=True, max_length=500, null=True, verbose_name='项目详情说明')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发布时间')),
                ('start_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='开始时间')),
                ('dead_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='截止时间')),
                ('is_delete', models.BooleanField(default=0, verbose_name='是否删除')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击量')),
                ('love_num', models.IntegerField(default=0, verbose_name='关注人数')),
                ('support_num', models.IntegerField(default=0, verbose_name='支持人数')),
                ('user_desc', models.CharField(max_length=50, verbose_name='自我介绍')),
                ('user_detail', models.TextField(blank=True, max_length=500, null=True, verbose_name='详情自我介绍')),
                ('user_mobile', models.CharField(max_length=11, verbose_name='发起人电话')),
                ('service_mobile', models.CharField(max_length=14, verbose_name='客服电话')),
                ('yigou_zhanghao', models.CharField(blank=True, max_length=18, null=True, verbose_name='易付宝企业账号')),
                ('faren_id', models.CharField(blank=True, max_length=18, null=True, verbose_name='法人身份证号')),
                ('is_renzheng', models.BooleanField(default=0, verbose_name='是否认证')),
            ],
            options={
                'verbose_name': '项目详情',
                'verbose_name_plural': '项目详情',
            },
        ),
        migrations.CreateModel(
            name='ProjectsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='项目类别名称')),
                ('desc', models.TextField(blank=True, help_text='类别描述', max_length=100, null=True, verbose_name='商品详情')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '项目类别',
                'verbose_name_plural': '项目类别',
            },
        ),
        migrations.CreateModel(
            name='ProjectsDetailImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_image', models.ImageField(max_length=200, upload_to='projects/detaili/%y/%m/%d', verbose_name='项目详情图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Projects', verbose_name='项目')),
            ],
            options={
                'verbose_name': '项目详情图片',
                'verbose_name_plural': '项目详情图片',
            },
        ),
        migrations.CreateModel(
            name='SupportItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('实物回报', '实物回报'), ('虚拟物品回报', '虚拟物品回报')], max_length=20, verbose_name='回报类型')),
                ('support_funding', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='支持金额')),
                ('desc', models.TextField(max_length=200, verbose_name='回报内容')),
                ('image', models.ImageField(upload_to='supports/%y/%m/%d', verbose_name='回报说明图片')),
                ('nums', models.IntegerField(default=0, verbose_name='回报数量')),
                ('supported_nums', models.IntegerField(default=0, verbose_name='此回报已获支持数量')),
                ('is_restrict', models.BooleanField(default=0, verbose_name='是否限购')),
                ('restrict_nums', models.IntegerField(default=1, verbose_name='限购数量')),
                ('transport_cost', models.IntegerField(default=0, verbose_name='运费')),
                ('is_invoice', models.BooleanField(default=0, verbose_name='是否开发票')),
                ('result_time', models.IntegerField(default=0, verbose_name='回报时间')),
                ('is_delete', models.BooleanField(default=0, verbose_name='是否删除')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Projects', verbose_name='所属项目')),
            ],
            options={
                'verbose_name': '回报项目',
                'verbose_name_plural': '回报项目',
            },
        ),
        migrations.AddField(
            model_name='projects',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.ProjectsCategory', verbose_name='项目类别'),
        ),
        migrations.AddField(
            model_name='indexcategoryad',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Projects', verbose_name='所属项目'),
        ),
        migrations.AddField(
            model_name='bannerinfo',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Projects', verbose_name='所属项目'),
        ),
    ]
