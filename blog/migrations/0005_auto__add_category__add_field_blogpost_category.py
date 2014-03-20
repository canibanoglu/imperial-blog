# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'blog_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'blog', ['Category'])

        # Adding field 'BlogPost.category'
        db.add_column(u'blog_blogpost', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Category'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'blog_category')

        # Deleting field 'BlogPost.category'
        db.delete_column(u'blog_blogpost', 'category_id')


    models = {
        u'blog.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Category']", 'null': 'True'}),
            'comments_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'draft_status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'hacker_news_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'blog.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['blog']