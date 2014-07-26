from django.conf.urls import patterns, include, url

from django.contrib import admin

from mymelodynotebook.views import index,register,home,log_out

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mymelodynotebook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', index, name="index"),
    url(r'^register/$', register),
    url(r'^home/$', home),
    url(r'^log_out/$', log_out),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'authlogin.html'}),
    (r'^accounts/', include('registration.backends.default.urls')),
)
