# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from freecoinage.coins.view import currency

urlpatterns = [
    url(
        regex=r'^currency/$',
        view=currency.currencyListView.as_view(),
        name='currencyList'
    ),
    url(
        regex=r'^currency/(?P<slug>[\w|\W]+)$',
        view=currency.currencyDetailView.as_view(),
        name='currencyDetail'
    ),

]
