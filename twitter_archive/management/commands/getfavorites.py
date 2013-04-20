import calendar
import rfc822
import datetime
import pytz

import twitter
from django.core.management.base import BaseCommand
from django.conf import settings
from twitter_archive.models import Tweet
from twitter_archive.twitter_regex import include_all

api = twitter.Api()
utc = pytz.UTC


class Command(BaseCommand):
    args = ''
    help = 'Get all favorited Tweets'

    def handle(self, *args, **options):
        count = 1
        favs = []
        latest = None

        if Tweet.objects.count() > 0:  # if there already are imported tweets
            latest = Tweet.objects.latest('date').tweet_id

        while len(api.GetFavorites(settings.TWITTER_ACCOUNT, page=count, since_id=latest)) > 0:
            favs = favs + api.GetFavorites(settings.TWITTER_ACCOUNT, page=count, since_id=latest)
            count = count + 1

        # save it
        for tweet in favs:
            created_at = utc.localize(datetime.datetime.fromtimestamp(calendar.timegm(rfc822.parsedate(tweet.created_at))))

            new = Tweet.objects.create(
                tweet_id=int(tweet.id),
                text=include_all(tweet.text),
                user=tweet.user.name,
                date=created_at)
            new.save()

        print "%d favorites have been imported" % len(favs)
