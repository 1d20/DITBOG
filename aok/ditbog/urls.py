from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'apps.core.views.home'),
    url(r'^login/$', 'apps.guest.views.login'),
    url(r'^auth/$', 'apps.guest.views.auth'),
    url(r'^logout/$', 'apps.guest.views.logout'),
    url(r'^theme/', include('apps.theme.urls')),
    url(r'^admin/', include(admin.site.urls))
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        	'document_root': settings.MEDIA_ROOT}))