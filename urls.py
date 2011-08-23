from django.conf.urls.defaults import patterns, include, url
from centrom.views import *


from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# (so we can see CSS and Images while still developing) page 57 of the book developing website with django
site_media = os.path.join(
                          os.path.dirname(__file__), 'site_media'
                          )

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'centromedico.views.home', name='home'),
    # url(r'^centromedico/', include('centromedico.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    # Browsing
    (r'^$', main_page),
    (r'^specialty/(\w+)/$', specialty_page), # \w+ means any string consisting of alphanumeric characters
    
    
    
    # Site media
    # the new entry binds all URLs under the site media directory to Django's static file serving view
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': site_media}),
                       
                       
    # Admin interface
    (r'^admin/', include(admin.site.urls)),
)
