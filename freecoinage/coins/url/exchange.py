# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from freecoinage.coins.exchange import views

urlpatterns = [
   url(
        regex=r'^$',
        view=views.exchangeListView.as_view(),
        name='exchangeList'
    ),
    url(
        regex=r'^exchange/(?P<slug>[\w|\W]+)$',
        view=views.exchangeDetailView.as_view(),
        name='exchangeDetail'
    ),
]
