# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Market'
        db.create_table('theme_market', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('path_script', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('theme', ['Market'])

        # Adding model 'Engine'
        db.create_table('theme_engine', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('package_template_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('path_sertificate', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('pass_sertificate', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('path_source', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('path_info_appdf', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('path_script_screen', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('path_script_res', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('path_script_asset', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('theme', ['Engine'])

        # Adding model 'Language'
        db.create_table('theme_language', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_long', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name_short', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('theme', ['Language'])

        # Adding model 'TemplateDescription'
        db.create_table('theme_templatedescription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(related_name='templatedescription_language', to=orm['theme.Language'])),
            ('engine', self.gf('django.db.models.fields.related.ForeignKey')(related_name='templatedescription_engine', to=orm['theme.Engine'])),
            ('template_description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('theme', ['TemplateDescription'])

        # Adding model 'Theme'
        db.create_table('theme_theme', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('engine', self.gf('django.db.models.fields.related.ForeignKey')(related_name='theme_engine', to=orm['theme.Engine'])),
            ('version', self.gf('django.db.models.fields.CharField')(default='1.0', max_length=10)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('package_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('path_res_folder', self.gf('django.db.models.fields.files.FileField')(default=None, max_length=100)),
            ('path_asset_folder', self.gf('django.db.models.fields.files.FileField')(default=None, max_length=100)),
            ('ad_code', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('path_to_apk', self.gf('django.db.models.fields.files.FileField')(default=None, max_length=100)),
            ('date_add', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('theme', ['Theme'])

        # Adding model 'Description'
        db.create_table('theme_description', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(related_name='description_language', to=orm['theme.Language'])),
            ('theme', self.gf('django.db.models.fields.related.ForeignKey')(related_name='description_theme', to=orm['theme.Theme'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('keywords', self.gf('django.db.models.fields.TextField')(default=None)),
            ('path_short_description', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('path_full_description', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('feathures', self.gf('django.db.models.fields.TextField')(default='-</feathure><feathure>-</feathure><feathure>-')),
            ('path_app_icon', self.gf('django.db.models.fields.files.FileField')(default=None, max_length=100)),
            ('path_large_promo', self.gf('django.db.models.fields.files.FileField')(default=None, max_length=100)),
            ('path_screens_folder', self.gf('django.db.models.fields.files.FileField')(default=None, max_length=100)),
        ))
        db.send_create_signal('theme', ['Description'])

        # Adding model 'ThemeMarket'
        db.create_table('theme_thememarket', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('theme', self.gf('django.db.models.fields.related.ForeignKey')(related_name='thememarket_theme', to=orm['theme.Theme'])),
            ('market', self.gf('django.db.models.fields.related.ForeignKey')(related_name='thememarket_market', to=orm['theme.Market'])),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date_add', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('theme', ['ThemeMarket'])

        # Adding model 'Ads'
        db.create_table('theme_ads', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('gen_script', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('theme', ['Ads'])

        # Adding model 'ThemeAd'
        db.create_table('theme_themead', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('theme', self.gf('django.db.models.fields.related.ForeignKey')(related_name='themead_theme', to=orm['theme.Theme'])),
            ('ad', self.gf('django.db.models.fields.related.ForeignKey')(related_name='themead_ad', to=orm['theme.Ads'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('theme', ['ThemeAd'])


    def backwards(self, orm):
        # Deleting model 'Market'
        db.delete_table('theme_market')

        # Deleting model 'Engine'
        db.delete_table('theme_engine')

        # Deleting model 'Language'
        db.delete_table('theme_language')

        # Deleting model 'TemplateDescription'
        db.delete_table('theme_templatedescription')

        # Deleting model 'Theme'
        db.delete_table('theme_theme')

        # Deleting model 'Description'
        db.delete_table('theme_description')

        # Deleting model 'ThemeMarket'
        db.delete_table('theme_thememarket')

        # Deleting model 'Ads'
        db.delete_table('theme_ads')

        # Deleting model 'ThemeAd'
        db.delete_table('theme_themead')


    models = {
        'theme.ads': {
            'Meta': {'object_name': 'Ads'},
            'gen_script': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'theme.description': {
            'Meta': {'object_name': 'Description'},
            'feathures': ('django.db.models.fields.TextField', [], {'default': "'-</feathure><feathure>-</feathure><feathure>-'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'default': 'None'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'description_language'", 'to': "orm['theme.Language']"}),
            'path_app_icon': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100'}),
            'path_full_description': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'path_large_promo': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100'}),
            'path_screens_folder': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100'}),
            'path_short_description': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'description_theme'", 'to': "orm['theme.Theme']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'theme.engine': {
            'Meta': {'object_name': 'Engine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'package_template_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pass_sertificate': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'path_info_appdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'path_script_asset': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'path_script_res': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'path_script_screen': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'path_sertificate': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'path_source': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'theme.language': {
            'Meta': {'object_name': 'Language'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_long': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_short': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'theme.market': {
            'Meta': {'object_name': 'Market'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path_script': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'theme.templatedescription': {
            'Meta': {'object_name': 'TemplateDescription'},
            'engine': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'templatedescription_engine'", 'to': "orm['theme.Engine']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'templatedescription_language'", 'to': "orm['theme.Language']"}),
            'template_description': ('django.db.models.fields.TextField', [], {})
        },
        'theme.theme': {
            'Meta': {'object_name': 'Theme'},
            'ad_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'date_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'engine': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'theme_engine'", 'to': "orm['theme.Engine']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'package_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'path_asset_folder': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100'}),
            'path_res_folder': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100'}),
            'path_to_apk': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '10'})
        },
        'theme.themead': {
            'Meta': {'object_name': 'ThemeAd'},
            'ad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'themead_ad'", 'to': "orm['theme.Ads']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'themead_theme'", 'to': "orm['theme.Theme']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'theme.thememarket': {
            'Meta': {'object_name': 'ThemeMarket'},
            'date_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'market': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'thememarket_market'", 'to': "orm['theme.Market']"}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'thememarket_theme'", 'to': "orm['theme.Theme']"})
        }
    }

    complete_apps = ['theme']