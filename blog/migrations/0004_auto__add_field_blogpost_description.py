# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BlogPost.description'
        db.add_column(u'blog_blogpost', 'description',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BlogPost.description'
        db.delete_column(u'blog_blogpost', 'description')


    models = {
        u'blog.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'comments_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'draft_status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'hacker_news_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['blog']