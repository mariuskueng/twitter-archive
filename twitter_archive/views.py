from django.views.generic import TemplateView
from twitter_archive.models import Tweet, Tag


class Home(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        kwargs['tags'] = Tag.objects.all()
        kwargs['all'] = Tweet.objects.all().count()
        kwargs['tweets'] = Tweet.objects.all()
        return kwargs


class TagDetail(TemplateView):
    template_name = 'content.html'
    context_object_name = "tweets"

    def get_context_data(self, **kwargs):
        kwargs['tags'] = Tag.objects.all()
        kwargs['tweets'] = Tweet.objects.filter(tag=Tag.objects.get(slug=self.kwargs['slug']))
        kwargs['all'] = Tweet.objects.all().count()
        return kwargs


class TagList(TemplateView):
    template_name = 'content.html'
    context_object_name = "tweets"

    def get_context_data(self, **kwargs):
        kwargs['tags'] = Tag.objects.all()
        kwargs['all'] = Tweet.objects.all().count()
        kwargs['tweets'] = Tweet.objects.all()
        return kwargs
