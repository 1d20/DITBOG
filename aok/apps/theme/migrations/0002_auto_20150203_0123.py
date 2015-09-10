# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enginedownloaditems',
            old_name='type',
            new_name='item_type',
        ),
        migrations.AddField(
            model_name='enginedownloaditems',
            name='folder_type',
            field=models.IntegerField(default=1, choices=[(1, b'Resources'), (2, b'Assets')]),
            preserve_default=True,
        ),
    ]
