# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-10 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField(max_length=200, verbose_name='评论内容')),
                ('user_tel', models.CharField(max_length=20, verbose_name='用户手机号')),
                ('content_id', models.CharField(max_length=10, verbose_name='文章ID')),
                ('parent_id', models.SmallIntegerField(choices=[(1, '回复'), (2, '评论')], default=2)),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('updata_time', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=True, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '评论管理',
                'verbose_name_plural': '评论管理',
            },
        ),
    ]
