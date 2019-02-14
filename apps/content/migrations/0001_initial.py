# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-10 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_title', models.CharField(max_length=20, verbose_name='分类标题')),
                ('brief', models.TextField(max_length=200, verbose_name='简介')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('updata_time', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=True, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '文章分类管理',
                'verbose_name_plural': '文章分类管理',
            },
        ),
        migrations.CreateModel(
            name='ContentModle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con_title', models.CharField(max_length=20, verbose_name='文章标题')),
                ('brief', models.TextField(max_length=200, null=True, verbose_name='内容')),
                ('status', models.SmallIntegerField(choices=[(1, '发表'), (2, '未发表')], default=1)),
                ('score', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='所需积分')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('updata_time', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=True, verbose_name='是否删除')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Category', verbose_name='文章分类')),
            ],
            options={
                'verbose_name': '文章内容管理',
                'verbose_name_plural': '文章内容管理',
            },
        ),
        migrations.CreateModel(
            name='Docket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_title', models.CharField(max_length=20, verbose_name='标签名字')),
                ('brief', models.TextField(max_length=200, verbose_name='简介')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('updata_time', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=True, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '标签管理',
                'verbose_name_plural': '标签管理',
            },
        ),
        migrations.AddField(
            model_name='contentmodle',
            name='docket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Docket', verbose_name='标签'),
        ),
    ]
