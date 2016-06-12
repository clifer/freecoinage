# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.coinListView.as_view(),
        name='coinList'
    ),
    url(
        regex=r'^coin/(?P<slug>[\w|\W]+)$',
        view=views.coinDetailView.as_view(),
        name='coinDetail'
    ),
]
