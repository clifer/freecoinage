# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import *

urlpatterns = [
   url(
        regex=r'^$',
        view=miningPoolListView.as_view(),
        name='miningPoolList'
    ),
    url(
        regex=r'^miningpools/(?P<slug>[\w|\W]+)$',
        view=miningPoolDetailView.as_view(),
        name='miningPoolDetail'
    ),
    url(
        regex=r'^miningpooltypes/(?P<slug>[\w|\W]+)$',
        view=miningPoolTypeDetailView.as_view(),
        name='miningPoolTypeDetail'
    ),
]
