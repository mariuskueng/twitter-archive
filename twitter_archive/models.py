from django.db import models
from django.utils.timezone import now


class Tweet(models.Model):
    tweet_id = models.IntegerField('ID', null=True)
    text = models.TextField('Text')
    user = models.CharField('User', max_length=200)
    date = models.DateTimeField('Datum', null=True)
    created = models.DateTimeField('Erstellt', default=now())
    tag = models.ManyToManyField('Tag', related_name='tags', blank=True, null=True)

    class Meta:
        verbose_name = 'Tweet'
        verbose_name_plural = 'Tweets'
        ordering = ['-date']

    def __unicode__(self):
        return self.text


class Tag(models.Model):
    name = models.CharField('Name', max_length=200)
    slug = models.SlugField('Slug', unique=True, null=True)
    synonyms = models.TextField('Synonyme', null=True, blank=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __unicode__(self):
        return self.name
