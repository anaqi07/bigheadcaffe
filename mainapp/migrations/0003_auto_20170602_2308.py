# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-02 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20170602_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='powder',
            field=models.ManyToManyField(blank=True, to='mainapp.Powder'),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='syrup',
            field=models.ManyToManyField(blank=True, to='mainapp.Syrup'),
        ),
    ]
