from django.conf.urls import patterns, include, url

from django.contrib import admin

import os

from mymelodynotebook.views import index,home,view,edit,delete,add,password_change_done,password_reset_done, password_reset_complete
from mymelodynotebook import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mymelodynotebook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', index, name="index"),
    url(r'^home/$', home, name="home"),
    url(r'^add/$', add, name="add"),
    url(r'^view/(\d+)$', view, name="view"),
    url(r'^edit/(\d+)$', edit, name="edit"),
    url(r'^delete/(\d+)$', delete, name="delete"),
    url(r'^$', index, name="index"),
    url(r'^password_change_done$', password_change_done, name="password_change_done"),
    url(r'^password_reset_done$', password_reset_done, name="password_reset_done"),
    url(r'^password_reset_complete$', password_reset_complete, name="password_reset_complete"),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^media/documents/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.dirname(settings.MEDIA_ROOT)+'/documents'}),
)
