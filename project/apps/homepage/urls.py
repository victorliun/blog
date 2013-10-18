from django.conf.urls import patterns, include, url
from views import HomepageView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),
    
    url(r'^$', HomepageView.as_view(), name='home'),
)
