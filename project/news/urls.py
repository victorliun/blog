from django.conf.urls import patterns, url

urlpatterns = patterns("",
    url(r'^articles/(?P<year>\d{4})/$', 'news.views.year_archive'),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', 'news.views.month_archive'),
)
