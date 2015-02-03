# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('gen_script', models.FileField(upload_to=b'script_ads')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('keywords', models.TextField(default=None)),
                ('path_short_description', models.FileField(upload_to=b'short_description')),
                ('path_full_description', models.FileField(upload_to=b'full_description')),
                ('feathures', models.TextField(default=b'-</feathure><feathure>-</feathure><feathure>-')),
                ('path_app_icon', models.FileField(default=None, upload_to=b'app_icon')),
                ('path_large_promo', models.FileField(default=None, upload_to=b'large_promo')),
                ('path_screens_folder', models.FileField(default=None, upload_to=b'screens_folder')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('package_template_name', models.CharField(max_length=255)),
                ('path_sertificate', models.FileField(upload_to=b'sertificate')),
                ('pass_sertificate', models.CharField(max_length=255)),
                ('path_source', models.FileField(upload_to=b'source')),
                ('path_info_appdf', models.FileField(upload_to=b'info_appdf')),
                ('path_script_screen', models.FileField(upload_to=b'script_screen')),
                ('path_script_res', models.FileField(upload_to=b'script_res')),
                ('path_script_asset', models.FileField(upload_to=b'script_asset')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EngineDownloadItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(default=1, choices=[(1, b'Image')])),
                ('count', models.IntegerField(default=1)),
                ('value', models.CharField(max_length=255)),
                ('engine', models.ForeignKey(to='theme.Engine')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_long', models.CharField(max_length=255)),
                ('name_short', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('path_script', models.FileField(upload_to=b'market')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TemplateDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('template_description', models.TextField()),
                ('engine', models.ForeignKey(related_name='templatedescription_engine', to='theme.Engine')),
                ('language', models.ForeignKey(related_name='templatedescription_language', to='theme.Language')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(default=b'1.0', max_length=10)),
                ('title', models.CharField(max_length=25)),
                ('package_name', models.CharField(max_length=255)),
                ('path_res_folder', models.FileField(default=None, upload_to=b'res')),
                ('path_asset_folder', models.FileField(default=None, upload_to=b'asset')),
                ('ad_code', models.CharField(default=b'', max_length=255)),
                ('path_to_apk', models.FileField(default=None, upload_to=b'apk')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('engine', models.ForeignKey(related_name='theme_engine', to='theme.Engine')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ThemeAd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=255)),
                ('ad', models.ForeignKey(related_name='themead_ad', to='theme.Ads')),
                ('theme', models.ForeignKey(related_name='themead_theme', to='theme.Theme')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ThemeDownloadItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.FileField(upload_to=b'theme_items')),
                ('engine_item', models.ForeignKey(to='theme.EngineDownloadItems')),
                ('theme', models.ForeignKey(to='theme.Theme')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ThemeMarket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info', models.CharField(max_length=255)),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('market', models.ForeignKey(related_name='thememarket_market', to='theme.Market')),
                ('theme', models.ForeignKey(related_name='thememarket_theme', to='theme.Theme')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='description',
            name='language',
            field=models.ForeignKey(related_name='description_language', to='theme.Language'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='theme',
            field=models.ForeignKey(related_name='description_theme', to='theme.Theme'),
            preserve_default=True,
        ),
    ]
