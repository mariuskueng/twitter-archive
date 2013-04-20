from django.contrib import admin
from twitter_archive.models import Tag, Tweet
from django.core.management import call_command


class TweetAdmin(admin.ModelAdmin):
    list_display = ['text', 'user', 'date', 'created']
    search_fields = ['text']


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    def save_model(self, request, obj, form, change):
        call_command('updatetags')
        obj.save()


admin.site.register(Tag, TagAdmin)
admin.site.register(Tweet, TweetAdmin)
