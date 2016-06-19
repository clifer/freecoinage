# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from autoslug import AutoSlugField
from freecoinage.coins.models import Coin, MinerType, MiningPoolType


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    @property
    def coins(self):
        coins = UserCoin.objects.filter(user = self.id)
        return coins

    @property
    def miners(self):
        miners = UserMiner.objects.filter(user = self.id)
        return miners

    @property
    def miningpools(self):
        miningpools = UserMiningPool.objects.filter(user = self.id)
        return miningpools

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in User._meta.fields]

@python_2_unicode_compatible
class UserCoin(models.Model):

    user = models.ForeignKey('User', related_name='UserUserCoins')
    coin = models.ForeignKey(Coin, related_name='UserCoins')
    active = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='self.id',always_update=True)
    slug_field = 'id'
    slug_url_kwarg = 'id'

    @property
    def name(self):
        return self.coin.name

    class Meta:
        unique_together = (('user'),('coin'))

    def __str__(self):
        return self.coin.name

    def get_absolute_url(self):
        return reverse('users:myCoinDetail', kwargs={'slug': self.slug)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in UserCoin._meta.fields]

class UserMiner(models.Model):
    name = models.CharField(max_length=30,blank=False)
    user = models.ForeignKey(User)
    minertype = models.ForeignKey(MinerType)
    host = models.CharField(max_length=30,blank=False)
    port = models.CharField(max_length=30,blank=False)
    apiurl = models.CharField(max_length=30,blank=False)
    apiuser = models.CharField(max_length=30,blank=False)
    apipass = models.CharField(max_length=30,blank=False)
    active = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='name',always_update=True)
    slug_field = 'name'
    slug_url_kwarg = 'name'

    class Meta:
        unique_together = (('host', 'port'),)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def get_absolute_url(self):
        return reverse('users:minerDetail', kwargs={'slug': self.slug})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in UserMiner._meta.fields]

class UserMiningPool(models.Model):
    name = models.CharField(max_length=30,blank=False)
    user = models.ForeignKey(User)
    description = models.CharField(max_length=1024,blank=True,null=True)
    host = models.CharField(max_length=30,null=True,blank=True)
    address = models.CharField(max_length=256,null=True,blank=True)
    port = models.CharField(max_length=30,null=True,blank=True)
    apiurl = models.CharField(max_length=256,null=True,blank=True)
    apikey = models.CharField(max_length=256,null=True,blank=True)
    pooltype = models.ForeignKey(MiningPoolType)
    active = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='name',always_update=True)
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def poolstats(self):
        apiresults = self.apiresults()
        poolstats = {'apiresults': apiresults,
                     'numcoins': 100,
                     'totalhashrate': 1000000,
                    }
        return poolstats

    def apiresults(self):
        apiresults = None
        if self.active and self.pooltype:
            from freecoinage.coin.miningpools import MiningPool
            miningpool = MiningPool(self)
            apiresults = miningpool.defaultapi()
        return apiresults

    def get_absolute_url(self):
        return reverse('users:miningPoolDetail', kwargs={'slug': self.slug})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in UserMiningPool._meta.fields]


