# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tweet'
        db.create_table(u'twitter_archive_tweet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 4, 18, 0, 0))),
        ))
        db.send_create_signal(u'twitter_archive', ['Tweet'])

        # Adding M2M table for field tag on 'Tweet'
        db.create_table(u'twitter_archive_tweet_tag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tweet', models.ForeignKey(orm[u'twitter_archive.tweet'], null=False)),
            ('tag', models.ForeignKey(orm[u'twitter_archive.tag'], null=False))
        ))
        db.create_unique(u'twitter_archive_tweet_tag', ['tweet_id', 'tag_id'])

        # Adding model 'Tag'
        db.create_table(u'twitter_archive_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'twitter_archive', ['Tag'])


    def backwards(self, orm):
        # Deleting model 'Tweet'
        db.delete_table(u'twitter_archive_tweet')

        # Removing M2M table for field tag on 'Tweet'
        db.delete_table('twitter_archive_tweet_tag')

        # Deleting model 'Tag'
        db.delete_table(u'twitter_archive_tag')


    models = {
        u'twitter_archive.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'twitter_archive.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 18, 0, 0)'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'tags'", 'null': 'True', 'to': u"orm['twitter_archive.Tag']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['twitter_archive']