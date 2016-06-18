from django.db import models
from decimal import Decimal
from autoslug import AutoSlugField
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


class Currency(models.Model):
    name = models.CharField(max_length=30,blank=False)
    symbol = models.CharField(max_length=30,blank=False)
    alt_symbol = models.CharField(max_length=30,null=True,blank=True)
    active = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='name',always_update=True)
    slug_field = 'symbol'
    slug_url_kwarg = 'symbol'

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def get_absolute_url(self):
        return reverse('exchanges:currencyDetail', kwargs={'slug': self.slug})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Currency._meta.fields]


class Algorithm(models.Model):
    name = models.CharField(max_length=30,unique=True,blank=False)
    active = models.BooleanField(default=False)
    description = models.CharField(max_length=1024,blank=True,null=True)
    slug = AutoSlugField(populate_from='name',always_update=True)
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    @property
    def coins(self):
        coins = Coin.objects.filter(algorithm = self.id)
        return coins

    def get_absolute_url(self):
        return reverse('algorithms:algorithmDetail', kwargs={'slug': self.slug})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Algorithm._meta.fields]


class Coin(models.Model):

    name = models.CharField(max_length=64,blank=False)
    symbol = models.CharField(max_length=30,blank=False)
    algorithm = models.ForeignKey(Algorithm)
    alt_symbol = models.CharField(max_length=30,null=True,blank=True)
    code = models.CharField(max_length=256,null=True,blank=True)
    logo = models.CharField(max_length=256,null=True,blank=True)
    pair = models.CharField(max_length=64,null=True)
    active = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='name',always_update=True)
    slug_field = 'name'
    slug_url_kwarg = 'name'

#    class Meta:
#        unique_together = (('symbol', 'algorithm'),)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    @property
    def markets(self):
        markets = Market.objects.filter(coinid = self.id)
        return markets

    @property
    def exchanges(self):
        exchanges = []
        for market in self.markets:
            exchanges.append(market.exchangeid)
        return exchanges


    @property
    def daemons(self):
        daemons = Daemon.objects.filter(coinid = self.id)
        return daemons

    def marketlogs(self):              # __unicode__ on Python 2
        for market in self.markets:
           marketlogs = market.marketlogs()
        return marketlogs

    def get_absolute_url(self):
        return reverse('coins:coinDetail', kwargs={'slug': self.slug})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Coin._meta.fields]


class Exchange(models.Model):
    name = models.CharField(unique=True,max_length=30,blank=False)
    apihostname = models.CharField(max_length=256,null=True,blank=True)
    apimarketsapi = models.CharField(max_length=256,null=True,blank=True)
    apimarketmapname = models.CharField(max_length=256,null=True,blank=True)
    apimarketmapid = models.CharField(max_length=256,null=True,blank=True)
    apicurrencyapi = models.CharField(max_length=256,null=True,blank=True)
    apiresults = models.CharField(max_length=30,null=True,blank=True)
    apimapname = models.CharField(max_length=30,null=True,blank=True)
    apimapsymbol = models.CharField(max_length=30,null=True,blank=True)
    apimapalgo = models.CharField(max_length=30,null=True,blank=True)
    url = models.CharField(max_length=256,null=True,blank=True)
    afflink = models.CharField(max_length=256,null=True,blank=True)
    active = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='name',always_update=True)
    slug_field = 'name'
    slug_url_kwarg = 'name'


#    class Meta:
#        unique_together = (('symbol', 'algorithm'),)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def getcurrencies(self):
        apiresults = None
        if self.active:
            from .exchanges.module import Exchange
            exchange = Exchange(self)
            apiresults = exchange.getcurrencies()
        return apiresults

    def getmarkets(self):
        apiresults = None
        if self.active:
            from .exchanges.module import Exchange
            thisexchange = Exchange(self)
            apiresults = thisexchange.getmarkets()
        return apiresults

    def get_absolute_url(self):
        return reverse('exchanges:exchangeDetail', kwargs={'slug': self.slug})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Exchange._meta.fields]

    @property
    def markets(self):
        markets = Market.objects.filter(exchangeid = self.id)
        return markets

    @property
    def currencies(self):
        currencies = []
        for market in self.markets:
            currencies.append(market.currencyid)
        return set(currencies)



class InfoService(models.Model):
    name = models.CharField(max_length=30,blank=False)
    apihostname = models.CharField(max_length=256,null=True,blank=True)
    apimarketsapi = models.CharField(max_length=256,null=True,blank=True)
    apicurrencyapi = models.CharField(max_length=256,null=True,blank=True)
    apiresults = models.CharField(max_length=30,null=True,blank=True)
    apimapname = models.CharField(max_length=30,null=True,blank=True)
    apimapsymbol = models.CharField(max_length=30,null=True,blank=True)
    apimapalgo = models.CharField(max_length=30,null=True,blank=True)
    url = models.CharField(max_length=256,null=True,blank=True)
    afflink = models.CharField(max_length=256,null=True,blank=True)
    active = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='name',always_update=True)
    slug_field = 'name'
    slug_url_kwarg = 'name'

#    class Meta:
#        unique_together = (('symbol', 'algorithm'),)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def get_absolute_url(self):
        return reverse('coins:infoserviceDetail', kwargs={'slug': self.slug})

class MinerType(models.Model):
    name = models.CharField(max_length=30,blank=False)
    description = models.CharField(max_length=1024,blank=True,null=True)
    slug = AutoSlugField(populate_from='name',always_update=True)
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def get_absolute_url(self):
        return reverse('miners:minerTypeDetail', kwargs={'slug': self.slug})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in MinerType._meta.fields]

class Miner(models.Model):
    name = models.CharField(max_length=30,blank=False)
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
        return reverse('miners:minerDetail', kwargs={'slug': self.slug})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Miner._meta.fields]

class MiningPoolType(models.Model):
    name = models.CharField(max_length=30,blank=False)
    description = models.CharField(max_length=1024,blank=True,null=True)
    slug = AutoSlugField(populate_from='name',always_update=True)
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def get_absolute_url(self):
        return reverse('miningpools:miningPoolTypeDetail', kwargs={'slug': self.slug})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in MiningPoolType._meta.fields]

class MiningPool(models.Model):
    name = models.CharField(max_length=30,blank=False)
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
            from bitscoins.miningpool import MiningPool
            miningpool = MiningPool(self)
            apiresults = miningpool.defaultapi()
        return apiresults

    def get_absolute_url(self):
        return reverse('miningpools:miningPoolDetail', kwargs={'slug': self.slug})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in MiningPool._meta.fields]

class Market(models.Model):
    name = models.CharField(max_length=30,blank=False)
    coinid = models.ForeignKey(Coin)
    currencyid = models.ForeignKey(Currency)
    exchangeid = models.ForeignKey(Exchange)
    marketcode = models.CharField(max_length=30,blank=True,null=True)
    marketcode2 = models.CharField(max_length=30,blank=True,null=True)
    exchangecoincode = models.CharField(max_length=30,blank=True,null=True)
    exchangecoincode2 = models.CharField(max_length=30,blank=True,null=True)
    exchangecurrencycode = models.CharField(max_length=30,blank=True,null=True)
    exchangecurrencycode2 = models.CharField(max_length=30,blank=True,null=True)
    volume_coin = models.DecimalField(max_digits=24, decimal_places=8,blank=True,null=True)
    volume_currency = models.DecimalField(max_digits=24, decimal_places=8,blank=True,null=True)
    price_low = models.DecimalField(max_digits=24, decimal_places=8,blank=True,null=True)
    price_high = models.DecimalField(max_digits=24, decimal_places=8,blank=True,null=True)
    active = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='name',always_update=True)
    slug_field = 'name'
    slug_url_kwarg = 'name'

    @property
    def exchanges(self):
        markets = Market.objects.filter(coinid = self.coinid)
        exchanges = []
        for market in markets:
            exchanges.append(market.exchangeid)
        return exchanges

    def marketlogs(self):              # __unicode__ on Python 2
#       marketlogs = MarketLog.objects.filter(marketid=self.id).order_by('created')
       marketlogs = []
       return marketlogs

    class Meta:
        unique_together = (('coinid', 'currencyid', 'exchangeid'),)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.coinid.symbol) + ' / ' + str(self.currencyid.symbol)

    def get_absolute_url(self):
        return reverse('markets:marketDetail', kwargs={'slug': self.slug})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Market._meta.fields]

class MarketLog(models.Model):
    marketid = models.ForeignKey(Market)
    volume_coin = models.DecimalField(max_digits=24, decimal_places=8,blank=True,null=True)
    volume_currency = models.DecimalField(max_digits=24, decimal_places=8,blank=True,null=True)
    price_low = models.DecimalField(max_digits=24, decimal_places=8,blank=True,null=True)
    price_high = models.DecimalField(max_digits=24, decimal_places=8,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)


class Daemon(models.Model):
    name = models.CharField(max_length=30,blank=False)
    coinid = models.ForeignKey(Coin)
    host = models.CharField(max_length=256,blank=True,null=True)
    port = models.IntegerField(blank=True,null=True)
    rpcport = models.IntegerField(blank=True,null=True)
    rpcuser = models.CharField(max_length=256,blank=True)
    rpcpassword = models.CharField(max_length=256,blank=True)
    balance = models.DecimalField(max_digits=24, decimal_places=8,blank=True,null=True)
#    accounts = ArrayField(models.CharField(max_length=256,null=True,blank=True))
#    accounts = hstore.DictionaryField()
    active = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='name',always_update=True)
    slug_field = 'name'
    slug_url_kwarg = 'name'

#    objects = hstore.HStoreManager()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def get_absolute_url(self):
        return reverse('coins:daemonDetail', kwargs={'slug': self.slug})

    @property
    def btcvalue(self):

        btcvalue =  0
        btcmarkets = Market.objects.filter(name__iexact=self.coinid.symbol + '_btc')
        if btcmarkets:
            btcvalue = btcmarkets[0].price_high * self.balance

        if self.coinid.symbol.lower() == 'btc':
            btcvalue =  self.balance

        return btcvalue

    def getaccountinfo(self):
        if self.active:
            from jsonrpc import ServiceProxy

            serverURL = 'http://' + str(self.rpcuser) + ':' + str(self.rpcpassword) + '@' + str(self.host) + ':' + str(self.rpcport)

            host = ServiceProxy(serverURL)
            try:
                self.accounts = host.listaccounts()
            except:
                self.accounts = {"": 0 }
            try:
                self.balance = host.getbalance()
            except:
                self.balance = 0

        return self.balance,self.accounts

    def info(self):
        info = {}
        if self.active:
            from jsonrpc import ServiceProxy

            serverURL = 'http://' + str(self.rpcuser) + ':' + str(self.rpcpassword) + '@' + str(self.host) + ':' + str(self.rpcport)

            host = ServiceProxy(serverURL)
            info = host.getinfo()

        return info

    def mininginfo(self):
        mininginfo = {}
        if self.active:
            from jsonrpc import ServiceProxy

            serverURL = 'http://' + str(self.rpcuser) + ':' + str(self.rpcpassword) + '@' + str(self.host) + ':' + str(self.rpcport)

            host = ServiceProxy(serverURL)
            mininginfo = host.getmininginfo()

        return mininginfo
