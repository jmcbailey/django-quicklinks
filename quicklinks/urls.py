from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'quicklinks.views.links', name='links'),
    url(r'^quicklinks/$', 'quicklinks.views.links', name='links'),
)
