from django.conf.urls import patterns, include, url

from django.contrib import admin

from mymelodynotebook.views import index,password_change_done,password_reset_done, password_reset_complete

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mymelodynotebook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', index, name="index"),
    url(r'^$', index, name="index"),
    url(r'^password_change_done$', password_change_done, name="password_change_done"),
    url(r'^password_reset_done$', password_reset_done, name="password_reset_done"),
    url(r'^password_reset_complete$', password_reset_complete, name="password_reset_complete"),
    (r'^accounts/', include('registration.backends.default.urls')),
)
