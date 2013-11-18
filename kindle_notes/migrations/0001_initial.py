# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table(u'kindle_notes_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=750)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=750)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'kindle_notes', ['Book'])

        # Adding model 'Note'
        db.create_table(u'kindle_notes_note', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('highlight', self.gf('django.db.models.fields.TextField')()),
            ('note', self.gf('django.db.models.fields.TextField')()),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kindle_notes.Book'])),
        ))
        db.send_create_signal(u'kindle_notes', ['Note'])


    def backwards(self, orm):
        # Deleting model 'Book'
        db.delete_table(u'kindle_notes_book')

        # Deleting model 'Note'
        db.delete_table(u'kindle_notes_note')


    models = {
        u'kindle_notes.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '750'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '750'})
        },
        u'kindle_notes.note': {
            'Meta': {'object_name': 'Note'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['kindle_notes.Book']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'highlight': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['kindle_notes']