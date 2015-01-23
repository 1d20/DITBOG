# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mail'
        db.create_table('mail_mail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('login', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('server', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_check', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('mail', ['Mail'])

        # Adding model 'MarketEngine'
        db.create_table('mail_marketengine', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('market', self.gf('django.db.models.fields.related.ForeignKey')(related_name='marketengine_market', to=orm['theme.Market'])),
            ('engine', self.gf('django.db.models.fields.related.ForeignKey')(related_name='marketengine_engine', to=orm['theme.Engine'])),
            ('mail', self.gf('django.db.models.fields.related.ForeignKey')(related_name='marketengine_mail', to=orm['mail.Mail'])),
            ('market_login', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('market_pass', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('mail', ['MarketEngine'])

        # Adding model 'Message'
        db.create_table('mail_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mail', self.gf('django.db.models.fields.related.ForeignKey')(related_name='message_mail', to=orm['mail.Mail'])),
            ('sender', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('new', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('mail', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Mail'
        db.delete_table('mail_mail')

        # Deleting model 'MarketEngine'
        db.delete_table('mail_marketengine')

        # Deleting model 'Message'
        db.delete_table('mail_message')


    models = {
        'mail.mail': {
            'Meta': {'object_name': 'Mail'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_check': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'server': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'mail.marketengine': {
            'Meta': {'object_name': 'MarketEngine'},
            'engine': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'marketengine_engine'", 'to': "orm['theme.Engine']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'marketengine_mail'", 'to': "orm['mail.Mail']"}),
            'market': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'marketengine_market'", 'to': "orm['theme.Market']"}),
            'market_login': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'market_pass': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'mail.message': {
            'Meta': {'object_name': 'Message'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message_mail'", 'to': "orm['mail.Mail']"}),
            'new': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
        'theme.market': {
            'Meta': {'object_name': 'Market'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path_script': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['mail']