# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.shortcuts import render, render_to_response

from django.contrib.auth.mixins import LoginRequiredMixin

from freecoinage.users.models import User
from freecoinage.coins.models import Miner, MinerType

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


class minerTypeDetailView(DetailView):
    model = MinerType
    # These next two lines tell the view to index lookups by slug
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class minerTypeRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('minertypes:minerTypeDetail',
                       kwargs={'slug': self.slug})

class minerTypeListView(ListView):
    model = MinerType
    # These next two lines tell the view to index lookups by slug
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


