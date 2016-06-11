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

class algorithmDetailView(LoginRequiredMixin, DetailView):
    model = Algorithm
    # These next two lines tell the view to index lookups by slug
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class algorithmRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('coins:algorithmDetail',
                       kwargs={'slug': self.slug})

class algorithmListView(LoginRequiredMixin, ListView):
    model = Algorithm
    # These next two lines tell the view to index lookups by slug
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class minerDetailView(LoginRequiredMixin, DetailView):
    model = Miner
    # These next two lines tell the view to index lookups by slug
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class minerRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('coins:minerDetail',
                       kwargs={'slug': self.slug})

class minerListView(LoginRequiredMixin, ListView):
    model = Miner
    # These next two lines tell the view to index lookups by slug
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class miningPoolDetailView(LoginRequiredMixin, DetailView):
    model = MiningPool
    # These next two lines tell the view to index lookups by slug
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class miningPoolRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('coins:miningPoolDetail',
                       kwargs={'slug': self.slug})

class miningPoolListView(LoginRequiredMixin, ListView):
    model = MiningPool
    # These next two lines tell the view to index lookups by slug
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class exchangeDetailView(LoginRequiredMixin, DetailView):
    model = Exchange
    # These next two lines tell the view to index lookups by slug
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class exchangeRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('exchanges:exchangeDetail',
                       kwargs={'slug': self.slug})

class exchangeListView(LoginRequiredMixin, ListView):
    model = Exchange
    # These next two lines tell the view to index lookups by slug
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class marketDetailView(LoginRequiredMixin, DetailView):
    model = Market
    # These next two lines tell the view to index lookups by slug
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class marketRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('markets:marketDetail',
                       kwargs={'slug': self.slug})

class marketListView(LoginRequiredMixin, ListView):
    model = Market
    # These next two lines tell the view to index lookups by slug
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class daemonDetailView(LoginRequiredMixin, DetailView):
    model = Daemon
    # These next two lines tell the view to index lookups by slug
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class daemonRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('coins:daemonDetail',
                       kwargs={'slug': self.slug})

class daemonListView(LoginRequiredMixin, ListView):
    model = Daemon
    # These next two lines tell the view to index lookups by slug
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

