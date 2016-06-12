# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import *

urlpatterns = [
   url(
        regex=r'^$',
        view=exchangeListView.as_view(),
        name='exchangeList'
    ),
    url(
        regex=r'^exchange/(?P<slug>[\w|\W]+)$',
        view=exchangeDetailView.as_view(),
        name='exchangeDetail'
    ),
]
