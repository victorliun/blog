from django.conf.urls import patterns, include, url
from views import homepage_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),
    
    url(r'^$', homepage_view, name='home'),
)
