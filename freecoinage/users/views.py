# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User, UserCoin, UserMiner, UserMiningPool


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name',]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserCoinDetailView(LoginRequiredMixin, DetailView):
    model = UserCoin
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class UserCoinRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:myCoinDetail',
                       kwargs={'slug': self.slug})


class UserCoinUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['coin',]

    # we already imported User in the view code above, remember?
    model = UserCoin

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:myCoinDetail',
                       kwargs={'slug': self.slug})

    def get_object(self):
        # Only get the User record for the user making the request
        return UserCoin.objects.get(slug=self.slug)


class UserCoinListView(LoginRequiredMixin, ListView):
    model = UserCoin
    # These next two lines tell the view to index lookups by username
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
