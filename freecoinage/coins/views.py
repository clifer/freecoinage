# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.shortcuts import render, render_to_response

from django.contrib.auth.mixins import LoginRequiredMixin

from freecoinage.users.models import User
from .models import Coin, Currency, Algorithm, Daemon, Market, Exchange, Miner, MiningPool


class coinDetailView(LoginRequiredMixin, DetailView):
    model = Coin
    # These next two lines tell the view to index lookups by slug
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class coinRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('coins:coinDetail',
                       kwargs={'slug': self.slug})

class coinListView(LoginRequiredMixin, ListView):
    model = Coin
    # These next two lines tell the view to index lookups by slug
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class coinListView2(LoginRequiredMixin, ListView):
#    model = Coin
    queryset = Coin.objects.all()

    # These next two lines tell the view to index lookups by slug
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_object(self):
        object = super(coinListView, self).get_object()
        object.markets = object.markets()
        object.save()
        # Return the object
        return object
