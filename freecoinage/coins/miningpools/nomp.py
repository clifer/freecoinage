from django.conf import settings
from freecoinage.coins.models import Daemon
from freecoinage.coins.util.apidatasource import FetchAPI

def defaultapi(mp):
    thispool = FetchAPI(str(mp.address) + ':' + str(mp.port), mp.apiurl)

    apiresults = []

    for coin in thispool['pools']:
        pool={}
        pool['name'] = thispool['pools'][coin]['name']
        pool['symbol'] = thispool['pools'][coin]['symbol']
        pool['algo'] = thispool['pools'][coin]['algorithm']
        pool['hashrate'] = thispool['pools'][coin]['hashrate']
        pool['blocks'] = thispool['pools'][coin]['blocks']
        pool['workers'] = thispool['pools'][coin]['workers']
        pool['poolstats'] = thispool['pools'][coin]['poolStats']
        daemons = Daemon.objects.filter()
        for daemon in daemons:
            if daemon.coinid.symbol ==  pool['symbol'] and daemon.active:
                try:
                    dm = daemon.mininginfo()
                except:
                    pass
                try:
                    pool['networkhashrate'] = dm['networkhashps']
                except:
                    pool['networkhashrate'] = thispool['pools'][coin]['hashrate']

                try:
                    pool['difficulty'] =  dm['difficulty']
                except:
                    pool['difficulty'] = None

        apiresults.append( pool )

    return apiresults
