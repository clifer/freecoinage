from django.conf import settings


class Exchange:
    def __init__(self, exchange):
            from pprint import pprint
            import time
            import importlib
            self.exchange = None
            self.name = exchange.name
            self.thisexchange = exchange
            self.apihostname = exchange.apihostname
            self.apicurrencyapi = exchange.apicurrencyapi
            self.apimarketsapi = exchange.apimarketsapi
            self.apimarketmapname = exchange.apimarketmapname
            self.apiresults = exchange.apiresults
            self.exchange = importlib.import_module("freecoinage.coins.exchanges.%s" % exchange.name.lower())

    def getcurrencies(self):
            apiresults = self.exchange.getcurrencies(self)
            return apiresults

    def getcurrency(self, coin):
            apiresults = self.exchange.getcurrency(self, coin)
            return apiresults

    def getmarkets(self):
            apiresults = self.exchange.getmarkets(self)
            return apiresults

    def getmarket(self, market):
            apiresults = self.exchange.getmarket(self, market)
            return apiresults
