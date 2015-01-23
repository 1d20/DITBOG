from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'mails/$', views.all),
    url(r'mails/(?P<mail_id>\d+)/$', views.all),
)
