from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'wall.views.home', name='home'),
    url(r'^event/$', 'wall.views.show_events', name='event'),
    url(r'^event/(?P<event_url>.+)', 'wall.views.display_event', name='event'),
)
