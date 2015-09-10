# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0002_auto_20150203_0123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='feathures',
        ),
        migrations.RemoveField(
            model_name='description',
            name='path_full_description',
        ),
        migrations.RemoveField(
            model_name='description',
            name='path_short_description',
        ),
        migrations.AddField(
            model_name='description',
            name='features',
            field=models.TextField(default=b'-</feature><feature>-</feature><feature>-'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='full_description',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='short_description',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
