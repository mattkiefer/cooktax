from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#import pdb; pdb.set_trace()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cooktax.views.home', name='home'),
    # url(r'^cooktax/', include('cooktax.foo.urls')),
    url(r'^lookup/(\d{13})','compare.views.lookup'),
    url(r'^/lookup/(\d{14})','compare.views.lookup'), # hack
    url(r'^/lookup2/','compare.views.lookup2', name="lookupfoo2"), # hack
    url(r'^/comps/(\d{13})','compare.views.comps'), 
    url(r'^/comps/(\d{14})','compare.views.comps'), 
    url(r'^/comps2/(\d{14})','compare.views.comps2'), # hack
    url(r'^/comps2/(\d{13})','compare.views.comps2'), # hack
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)


