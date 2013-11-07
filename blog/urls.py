from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^read/(?P<slug>[-\w]+)/$', views.read_article, name='read_article'),
        )
