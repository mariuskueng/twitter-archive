from django.conf.urls import patterns, include, url
from django.contrib import admin
from twitter_archive.views import Home, TagDetail, TagList

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^all/$', TagList.as_view(), name="list"),
    url(r'^tag/(?P<slug>[a-zA-Z0-9_\.-]+)/$', TagDetail.as_view(), name="detail"),
    url(r'^admin/', include(admin.site.urls)),
)
