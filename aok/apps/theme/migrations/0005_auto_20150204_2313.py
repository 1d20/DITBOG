# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0004_auto_20150203_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='enginedownloaditems',
            name='height',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='enginedownloaditems',
            name='required_count',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='enginedownloaditems',
            name='template_name',
            field=models.CharField(default=b'{0}', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='enginedownloaditems',
            name='width',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='enginedownloaditems',
            name='value',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
