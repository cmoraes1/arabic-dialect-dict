# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_auto_20171201_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='dialect',
            field=models.CharField(choices=[('levantine', 'levantine'), ('egyptian', 'egyptian'), ('gulf', 'gulf')], default='levantine', max_length=9),
            preserve_default=False,
        ),
    ]
