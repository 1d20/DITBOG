from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'themes/$', views.themes),
    url(r'themes/(?P<engine_id>\d+)/$', views.themes),
    url(r'zip/(?P<type>\w+)/$', views.zip),
    url(r'change/$', views.change),
    url(r'add/$', views.add),
    url(r'show/(?P<theme_id>\d+)/$', views.show),
)
