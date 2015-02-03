from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',

    url(r'themes/$', views.themes, name='themes'),
    url(r'themes/(?P<engine_id>\d+)/$', views.themes, name='themes-engine'),
    url(r'zip/(?P<type>\w+)/$', views.zip, name='theme-zip-type'),
    url(r'change/$', views.change, name='theme-change'),
    url(r'add/$', views.add, name='theme-add'),
    url(r'show/(?P<theme_id>\d+)/$', views.show, name='theme-show'),
    
    url(r'edit_description/(?P<desc_id>\d+)/$', views.edit_description),
)
