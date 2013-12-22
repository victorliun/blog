from django.conf.urls import patterns, url
from display.views import DisplayView
from editor.views import EditorView

urlpatterns = patterns('',
    url('^display/(?P<article_id>\d+)$', DisplayView.as_view(), name="display"),
    url('^display/new$', EditorView.as_view(), name="editor"),
)
