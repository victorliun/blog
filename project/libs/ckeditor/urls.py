from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'libs.ckeditor',
    url(r'^upload/', 'views.upload', name='ckeditor_upload'),
    url(r'^browse/', 'views.browse', name='ckeditor_browse'),
)
