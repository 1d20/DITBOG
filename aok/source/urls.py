from django.conf import settings
from django.conf.urls import include, url, static
from django.contrib import admin

from apps.core import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^auth/$', views.auth, name='auth'),
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^theme/', include('apps.theme.urls')),

    url(r'^admin/', include(admin.site.urls))
]

# if settings.DEBUG:
#     urlpatterns += [
#         static.static(r'^media/(?P<path>.*)$', document_root=settings.MEDIA_ROOT)  # TODO: Fix this
#     ]
