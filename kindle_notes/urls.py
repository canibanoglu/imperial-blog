from django.conf.urls import patterns, url
from kindle_notes import views

urlpatterns = patterns('',
        url(r'^$', views.books_index, name='books_index'),
        url(r'^upload/$', views.books_upload, name='books_upload'),
        url(r'^(?P<pk>[-\w]+)/view/$', views.books_view_notes, name='books_view_notes'),
        )

