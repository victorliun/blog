from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required as LG

from display.views import DisplayView
from editor.views import EditorView
from diary.views import *

urlpatterns = patterns('',
    url('^display/(?P<article_id>\d+)$', DisplayView.as_view(), name="display"),
    url('^display/new$', EditorView.as_view(), name="editor"),
)

urlpatterns += patterns('',
    url('^diary/new$', LG(CreateDiaryView.as_view()), {}, name="diary-new"),
    url('^diary/(?P<pk>\d+)/$', DetailDiaryView.as_view(), {}, name="diary-detail"),
    url('^diary/edit\?pk=(?P<pk>\d+)$', UpdateDiaryView.as_view(), {}, name="diary-edit"),
    url('^diary/delete/(?P<pk>\d+)$', DeleteDiaryView.as_view(), {}, name="diary-delete"),
    url('^diary/archive/rate=(?P<rate>)$', ListDiaryView.as_view(), {}, name="diary-list"),
    )