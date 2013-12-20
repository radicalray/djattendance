from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
#from reports.views import RosterTemplate

#Uncomment the next two lines to enable the admin:
from django.contrib import admin
import autofixture

admin.autodiscover()
autofixture.autodiscover()

urlpatterns = patterns('',

    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^$', 'ap.views.home'),
   	
    #url(r'^roster/$','reports.views.roster'),
       
    #url(r'^terms/', include('terms.urls', namespace="terms")),
    url(r'^reports/', include('reports.urls')),
    # url(r'^roster/$', 'reports.views.Roster'),
    # url(r'^roster_temp/$', 'reports.views.Roster_Temp'),
    # url(r'^roster_simple/$', 'reports.views.Roster_Temp_simple'),
    # url(r'^roster_class_view/$', RosterTemplate.as_view()),
    
    # Examples:
    # url(r'^$', 'ap.views.home', name='home'),
    # url(r'^ap/', include('ap.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

