import re

def include_links(text):
    r = re.compile(r"(http://[^ ]+)")
    text = r.sub(r'<a href="\1">\1</a>', text)
    return text

def include_mentions(text):
    r = re.compile(r"(@[^ ]+)")
    text = r.sub(r'<a href="http://twitter.com/\1">\1</a>', text)
    return text

def include_hashes(text):
    r = re.compile(r"(#[^ ]+)")
    text = r.sub(r'<a href="http://twitter.com/\1">\1</a>', text)
    return text

def include_all(text):
    text = include_links(text)
    text = include_mentions(text)
    text = include_hashes(text)
    return text
