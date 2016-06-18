# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import  Coin, Currency, Algorithm, Miner, MiningPool, MiningPoolType, Market, Daemon, Exchange
#from .models import UserCoin, Coin, Currency, Algorithm, Miner, MiningPool, MiningPoolType,  Market, Daemon, Exchange
from freecoinage.users.models import UserCoin


admin.site.register(Coin)
admin.site.register(UserCoin)
admin.site.register(Currency)
admin.site.register(Algorithm)
admin.site.register(Miner)
admin.site.register(MiningPoolType)
admin.site.register(MiningPool)
admin.site.register(Market)
admin.site.register(Daemon)
admin.site.register(Exchange)
