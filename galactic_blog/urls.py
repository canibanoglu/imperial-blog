from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'galactic_blog.views.home', name='home'),
    # url(r'^galactic_blog/', include('galactic_blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^sidious/', include(admin.site.urls)),
    url(r'^', include('blog.urls', 'blog', 'imperialblog')),
    url(r'^kindle/', include('kindle_notes.urls', 'kindle', 'kindle_notes')),
)

if not settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
