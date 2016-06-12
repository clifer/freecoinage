# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import *

urlpatterns = [
   url(
        regex=r'^$',
        view=minerListView.as_view(),
        name='minerList'
    ),
    url(
        regex=r'^miners/(?P<slug>[\w|\W]+)$',
        view=minerDetailView.as_view(),
        name='minerDetail'
    ),
]
