# Generated by Django 2.2.7 on 2021-09-10 15:30

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=100, verbose_name='标签')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
            ],
            options={
                'verbose_name': '标签表',
                'verbose_name_plural': '标签表',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('title', models.CharField(max_length=70, verbose_name='标题')),
                ('user', models.CharField(default='coinfamily', max_length=70, verbose_name='作者')),
                ('excerpt', models.TextField(default='', max_length=200, verbose_name='摘要')),
                ('img', models.ImageField(blank=True, null=True, upload_to='article/%Y/%m/%d/', verbose_name='文章图片')),
                ('body', DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='阅读量')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('tags', models.ManyToManyField(blank=True, null=True, to='blogs.Tag', verbose_name='标签')),
            ],
            options={
                'verbose_name': '找回方案文章',
                'verbose_name_plural': '找回方案文章',
            },
        ),
    ]
