# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-04 19:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='slug',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField()),
            ],
            options={
                'db_table': 'slugs',
            },
        ),
        migrations.CreateModel(
            name='lookup',
            fields=[
                ('slug_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='skinnyapp.slug')),
                ('when', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'lookups',
            },
        ),
    ]
