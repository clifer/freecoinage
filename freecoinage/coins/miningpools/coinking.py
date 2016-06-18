from django.conf import settings
from freecoinage.coins.models import Daemon
from freecounage.coins.util.apidatasource import FetchAPI


def defaultapi(mp):
    thispool = FetchAPI(str(mp.address) + ':' + str(mp.port), mp.apiurl)

    apiresults = [ 
    for coin in thispool:
        pool = {}
        pool['name'] = coin['name']
        pool['symbol'] = coin['nickname']
        pool['algo'] = coin['type']
        pool['difficulty'] = coin['difficulty']
        pool['hashrate'] = coin['hashrate']
        pool['blocks'] = {}
        pool['workers'] = {}
        pool['poolstats'] = {}
        pool['difficulty'] = coin['difficulty']

        daemons = Daemon.objects.filter()
        for daemon in daemons:
            if daemon.coinid.symbol ==  pool['symbol'] and daemon.active:
                try:
                    pool['networkhashrate'] = daemon.mininginfo['networkhashps']
                except:
                    pool['networkhashrate'] = coin['hashrate']




        apiresults.append( pool )

    return apiresults 
