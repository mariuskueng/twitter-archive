import re
from twitter_archive.models import Tweet

def include_links():
    for t in Tweet.objects.all():
        s = t.text
        r = re.compile(r"(http://[^ ]+)")
        t.text = r.sub(r'<a href="\1">\1</a>', s)
        t.save()

def include_mentions():
    for t in Tweet.objects.all():
        s = t.text
        r = re.compile(r"(@[^ ]+)")
        t.text = r.sub(r'<a href="http://twitter.com/\1">\1</a>', s)
        t.save()

def include_hashes():
    for t in Tweet.objects.all():
        s = t.text
        r = re.compile(r"(#[^ ]+)")
        t.text = r.sub(r'<a href="http://twitter.com/\1">\1</a>', s)
        t.save()
