# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Tag.synonyms'
        db.add_column(u'twitter_archive_tag', 'synonyms',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Tag.synonyms'
        db.delete_column(u'twitter_archive_tag', 'synonyms')


    models = {
        u'twitter_archive.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'synonyms': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'twitter_archive.tweet': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Tweet'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 18, 0, 0)'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'tags'", 'null': 'True', 'to': u"orm['twitter_archive.Tag']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'tweet_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['twitter_archive']