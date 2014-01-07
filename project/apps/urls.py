from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required as LG

from diary.views import *

urlpatterns = patterns('',
    url(r'^(home/)?', include('apps.homepage.urls')),
    url(r'^diary/new$', LG(CreateDiaryView.as_view()), {}, name="diary-new"),
    url(r'^diary/(?P<pk>\d+)/$', DetailDiaryView.as_view(), {}, name="diary-detail"),
    url(r'^diary/edit/(?P<pk>\d+)$', UpdateDiaryView.as_view(), {}, name="diary-edit"),
    url(r'^diary/delete/(?P<pk>\d+)$', DeleteDiaryView.as_view(), {}, name="diary-delete"),
    url(r'^diary/(?P<category>)$', ListDiaryView.as_view(), {}, name="diary-list"),
    )