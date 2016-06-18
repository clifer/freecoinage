from freecoinage.coins.util.apidatasource import FetchAPI

def getcurrencies(exchange):

    exchangeapi = FetchAPI(exchange.apihostname, exchange.apicurrencyapi)
    currencies =  exchangeapi[exchange.apiresults]

    normalized_currencies = []

    for coin in currencies:
        normalized_coin = { 'name': coin['Name'],
                            'algorithm': coin['Algorithm'],
                            'symbol': coin['Symbol'],
                            'code': coin['Id']#,
                          }
        normalized_currencies.append(normalized_coin)

    return normalized_currencies

def getcurrency(symbol):
    normalized_coin = { }
    return normalized_coin

def getmarket(marketname):
    normalized_market = { }
    return normalized_market

def getmarkets(exchange):
    exchangeapi = FetchAPI(exchange.apihostname, '/api/GetMarkets')
    markets =  exchangeapi[exchange.apiresults]

    normalized_markets = []

    for market in markets:
        market_name=str(market['Label'].replace('/','_'))
        coinids=market_name.rsplit('_')

        normalized_market = {'name': market_name,
                             'coin': coinids[0],
                             'currency': coinids[1],
                             'exchange': exchange.name,
                             'price_high': market['BidPrice'],
                             'price_low': market['AskPrice'],
                             'volume_currency': market['Volume'],
                            }

        normalized_markets.append(normalized_market)

    return normalized_markets

def updatemarkets(exchange):
#    exchangeapi = Cryptsy("", "")
#   markets = exchangeapi.markets()
    exchangeapi = FetchAPI(exchange.apihostname, '/api/GetMarkets')
    markets =  exchangeapi[exchange.apiresults]
    excurrencies =  getcurrencies(exchange)

#    print(exchange.apiresults)
    normalized_markets = []

    for exmarket in markets:
#        print(exmarket)
        market_name=str(exmarket['Label'].replace('/','_'))
        coinids=market_name.rsplit('_')
#        excoin = exchangeapi.currency(coinids[0])
#        print(coinids)
#        print(excurrencies)
        excoin={}
        for excurrency in excurrencies:
#            print(excurrency)
            if excurrency['symbol'].lower == coinids[0].lower():
                excoin=excurrency

        if excoin:
            coin, coin_created = CryptoCoin.objects.get_or_create(symbol__iexact=excoin['symbol'])

            algo = CryptoAlgorithm.objects.get(name__iexact=excoin['algorithm'])
            coin.algorithm=algo

            if coin_created:
                coinrank = CryptoCoinRank()
                coinrank.coinid = coin
                coin.name=excoin['name']
                coin.symbol=excoin['symbol']
                coin.code=excoin['code']
                coin.active=False
                coin.save()
                coinrank.save()

            coin.save()

            currency, currency_created = CryptoCurrency.objects.get_or_create(symbol__iexact=coinids[1])

            market, market_created = CryptoMarket.objects.get_or_create(coinid=coin, currencyid=currency, exchangeid=exchange.thisexchange)
            if market_created:
                market.coinid = coin
                market.currencyid = currency
                market.exchangeid = exchange.thisexchange
                market.name = market_name
                market.active = False

            market.price_high = Decimal(exmarket['BidPrice'])
            market.price_low =  Decimal(exmarket['AskPrice'])
            market.volume_currency =  Decimal(exmarket['Volume'])

            market.save()

#                "TradePairId":100,
#               "Label":"LTC/BTC",
#               "AskPrice":0.00006000,
#               "BidPrice":0.02000000,
#               "Low":0.00006000,
#               "High":0.00006000,
#               "Volume":1000.05639978,
#               "LastPrice":0.00006000,
#               "LastVolume":499.99640000,
#               "BuyVolume":34455.678,
#               "SellVolume":67003436.37658233,
#               "Change":-400.00000000

            normalized_market = {'name': market.name,
                                 'coin': market.coinid,
                                 'currency': market.currencyid,
                                 'exchange': market.exchangeid,
                                 'price_high': market.price_high,
                                 'price_low': market.price_low,
                                 'volume_currency': market.volume_currency,
                              }

            normalized_markets.append(normalized_market)

    return normalized_markets
