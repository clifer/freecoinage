# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import *

urlpatterns = [
    url(
        regex=r'^currency/$',
        view=currencyListView.as_view(),
        name='currencyList'
    ),
    url(
        regex=r'^currency/(?P<slug>[\w|\W]+)$',
        view=currencyDetailView.as_view(),
        name='currencyDetail'
    ),

]
