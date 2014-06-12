from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','Login.views.start', name = 'start'),
    url(r'^Login$','Login.views.register',name = 'register'),
    url(r'^process$','Login.views.process', name = 'process'),
    url(r'^admin/', include(admin.site.urls)),
)
