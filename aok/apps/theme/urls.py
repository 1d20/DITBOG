from django.conf.urls import url
import views

urlpatterns = [
    url(r'themes/$', views.themes, name='themes'),
    url(r'themes/(?P<engine_id>\d+)/$', views.themes, name='themes-engine'),
    url(r'zip/(?P<type>\w+)/$', views.zip, name='theme-zip-type'),
    url(r'change/$', views.change, name='theme-change'),
    url(r'add/$', views.add, name='theme-add'),
    url(r'show/(?P<theme_id>\d+)/$', views.show, name='theme-show'),

    url(r'desc/(?P<theme_id>\d+)/$', views.desc, name='theme-desc'),
    url(r'res/(?P<theme_id>\d+)/$', views.res, name='theme-res'),
    
    url(r'apk/(?P<theme_id>\d+)/$', views.apk, name='theme-apk'),
    url(r'appdf/(?P<theme_id>\d+)/$', views.appdf, name='theme-appdf'),


    url(r'edit_description/(?P<desc_id>\d+)/$', views.edit_description, name='theme-edit-description'),
]
