from django.conf.urls import patterns, include, url

from reports import views

urlpatterns = patterns('',
    url(r'^roster/$', views.index, name='index'),
    url(r'^roster(?P<roster_id>\d+)/$', views.detail, name='detail'),
    url(r'^roster(?P<roster_id>\d+)/results/$', views.results, name='results'),
    url(r'^roster(?P<roster_id>\d+)/vote/$', views.vote, name='vote'),
    
)

