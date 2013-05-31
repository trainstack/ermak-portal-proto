from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.conf.urls.defaults import *
from TrainStack.views import someview, crtuser, display, crtgroup, topo, tsk
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html', }),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}),
    (r'', include('django.contrib.auth.urls')),
    (r'^profile/$', display),
    (r'^admin/', include(admin.site.urls)),
    (r'^crt/', crtuser),
    (r'^crtg/', crtgroup),
    (r'^topo/', topo),
    (r'^tsk/', tsk),

)

    # Examples:
    # url(r'^$', 'TrainStack.views.home', name='home'),
    # url(r'^TrainStack/', include('TrainStack.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
