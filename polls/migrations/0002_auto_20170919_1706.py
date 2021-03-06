# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-19 14:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='state',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.State'),
        ),
    ]
