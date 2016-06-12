# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from freecoinage.coins import views

urlpatterns = [
   url(
        regex=r'^$',
        view=views.miningPoolListView.as_view(),
        name='miningPoolList'
    ),
    url(
        regex=r'^miningpools/(?P<slug>[\w|\W]+)$',
        view=views.miningPoolDetailView.as_view(),
        name='miningPoolDetail'
    ),
]
