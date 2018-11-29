# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-27 01:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Scopus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='source',
            field=models.ForeignKey(help_text='Where the document is published', on_delete=django.db.models.deletion.CASCADE, to='Scopus.Source'),
        ),
    ]