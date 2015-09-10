# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0003_auto_20150203_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engine',
            name='path_script_asset',
        ),
        migrations.RemoveField(
            model_name='engine',
            name='path_script_res',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='path_asset_folder',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='path_res_folder',
        ),
    ]
