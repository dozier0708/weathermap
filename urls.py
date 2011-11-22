from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','weather.events.views.homepage'),
    url(r'^weather/(?P<weather_id>\d+)/$', 'weather.events.views.detail'),
    url(r'^types/$', 'weather.events.views.event_type_list'),
    url(r'^types/(?P<type_id>\d+)/$', 'weather.events.views.event_type_detail'),
    url(r'^admin/', include(admin.site.urls)),
)
