# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import *

urlpatterns = [
   url(
        regex=r'^$',
        view=marketListView.as_view(),
        name='marketList'
    ),
    url(
        regex=r'^markets/(?P<slug>[\w|\W]+)$',
        view=marketDetailView.as_view(),
        name='marketDetail'
    ),
]
