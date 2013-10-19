from django.conf.urls import patterns, url
from display.views import DisplayView

urlpatterns = patterns('',
    url('^display/(?P<article_id>\d+)$', DisplayView.as_view(), name="display"),
)
