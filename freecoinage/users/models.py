# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from autoslug import AutoSlugField
from freecoinage.coins.models import Coin


@python_2_unicode_compatible
class UserCoin(models.Model):

    user = models.ForeignKey('User', related_name='UserUserCoins')
    coin = models.ForeignKey(Coin, related_name='UserCoins')
    active = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='name',always_update=True)
    slug_field = 'coin'
    slug_url_kwarg = 'coin'

    @property
    def name(self):
        return self.coin.name

    class Meta:
        unique_together = (('user'),('coin'))

    def __str__(self):
        return self.coin.name

    def get_absolute_url(self):
        return reverse('usercoin:detail', kwargs={'username': self.user.name, 'coin': self.coin.name})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in UserCoin._meta.fields]

@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    @property
    def coins(self):
        coins = UserCoin.objects.filter(user = self.id)
        return coins

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in User._meta.fields]
