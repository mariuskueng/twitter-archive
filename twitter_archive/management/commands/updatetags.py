from django.core.management.base import BaseCommand
from twitter_archive.models import Tweet, Tag

tweets = Tweet.objects.all()
tags = Tag.objects.all()


class Command(BaseCommand):
    args = ''
    help = 'Add Tags to Tweets'

    def handle(self, *args, **options):
        # go through all tweets in tag 'em
        count = 0
        for tweet in tweets:
            for tag in tags:
                synonyms = tag.synonyms.split()
                for s in synonyms:
                    if "%s " % s.lower() in tweet.text.lower():
                        count = count + 1
                        tweet.tag.add(tag)
                        tweet.save()

            # if no tag fits, put it into 'others'
            if not tweet.tag.all():
                if Tag.objects.get(slug='others'):
                    tweet.tag.add(Tag.objects.get(slug='others'))

        print '%d Tags have been added to tweets' % count
