# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-30 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Table', '0002_sometable_column3'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sometable',
            options={'managed': True},
        ),
        migrations.AlterField(
            model_name='sometable',
            name='column1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Столбик'),
        ),
        migrations.AlterField(
            model_name='sometable',
            name='column2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sometable',
            name='column3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterModelTable(
            name='sometable',
            table='SomeTable',
        ),
    ]