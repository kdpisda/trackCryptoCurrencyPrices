# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-10 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact_no',
            field=models.CharField(blank=True, default='0000000000', max_length=10),
        ),
    ]