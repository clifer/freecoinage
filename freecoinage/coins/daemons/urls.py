# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from freecoinage.coins import views

urlpatterns = [
   url(
        regex=r'^$',
        view=views.daemonListView.as_view(),
        name='daemonList'
    ),
    url(
        regex=r'^daemons/(?P<slug>[\w|\W]+)$',
        view=views.daemonDetailView.as_view(),
        name='daemonDetail'
    ),
]
