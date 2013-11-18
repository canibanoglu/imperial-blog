# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Note.location'
        db.add_column(u'kindle_notes_note', 'location',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Note.page'
        db.add_column(u'kindle_notes_note', 'page',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Note.location'
        db.delete_column(u'kindle_notes_note', 'location')

        # Deleting field 'Note.page'
        db.delete_column(u'kindle_notes_note', 'page')


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
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'page': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['kindle_notes']