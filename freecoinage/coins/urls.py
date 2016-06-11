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
    url(
        regex=r'^algorithm/$',
        view=views.algorithmListView.as_view(),
        name='algorithmList'
    ),
    url(
        regex=r'^algorithm/(?P<slug>[\w|\W]+)$',
        view=views.algorithmDetailView.as_view(),
        name='algorithmDetail'
    ),
    url(
        regex=r'^miner/$',
        view=views.minerListView.as_view(),
        name='minerList'
    ),
    url(
        regex=r'^miner/(?P<slug>[\w|\W]+)$',
        view=views.minerDetailView.as_view(),
        name='minerDetail'
    ),
    url(
        regex=r'^miningpool/$',
        view=views.miningPoolListView.as_view(),
        name='miningpoolList'
    ),
    url(
        regex=r'^miningpool/(?P<slug>[\w|\W]+)$',
        view=views.miningPoolDetailView.as_view(),
        name='miningPoolDetail'
    ),
    url(
        regex=r'^daemon/$',
        view=views.daemonListView.as_view(),
        name='daemonList'
    ),
    url(
        regex=r'^daemon/(?P<slug>[\w|\W]+)$',
        view=views.daemonDetailView.as_view(),
        name='daemonDetail'
    ),

]
