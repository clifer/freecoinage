# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.shortcuts import render, render_to_response

from django.contrib.auth.mixins import LoginRequiredMixin

from freecoinage.users.models import User
from freecoinage.coins.models import Market


class marketDetailView(DetailView):
    model = Market
    # These next two lines tell the view to index lookups by slug
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class marketRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('markets:marketDetail',
                       kwargs={'slug': self.slug})

class marketListView(ListView):
    model = Market
    # These next two lines tell the view to index lookups by slug
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
