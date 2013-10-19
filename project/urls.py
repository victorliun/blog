from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    (r'^display/P<article_id>\d+', displayer, name="displayer")),
)

urlpatterns += staticfiles_urlpatterns()
