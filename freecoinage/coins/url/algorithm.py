# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from freecoinage.coins import views

urlpatterns = [
   url(
        regex=r'^$',
        view=views.algorithmListView.as_view(),
        name='algorithmList'
    ),
    url(
        regex=r'^algorithms/(?P<slug>[\w|\W]+)$',
        view=views.algorithmDetailView.as_view(),
        name='algorithmDetail'
    ),
]
