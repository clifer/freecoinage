# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import *

urlpatterns = [
   url(
        regex=r'^$',
        view=algorithmListView.as_view(),
        name='algorithmList'
    ),
    url(
        regex=r'^algorithms/(?P<slug>[\w|\W]+)$',
        view=algorithmDetailView.as_view(),
        name='algorithmDetail'
    ),
]
