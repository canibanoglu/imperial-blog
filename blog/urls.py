from django.conf.urls import patterns, url
from blog import views
from blog.feed import LatestEntriesFeed

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^read/(?P<slug>[-\w]+)/$', views.read_article, name='read_article'),
        url(r'^archives/$', views.archives, name="archives"),
        url(r'^feed/$', LatestEntriesFeed(), name="feed"),
        url(r'^categories/$', views.categories, name="categories"),
        url(r'^inks/$', views.similar_inks, name="similar_inks"),
        )
