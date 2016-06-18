# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

def load_algorithms(apps, schema_editor):
    Algorithm = apps.get_model("coins", "Algorithm")
    sha256 = Algorithm(id=1,name='SHA256',active=True,description='SHA256',slug='sha256')
    sha256.save()
    scrypt = Algorithm(id=2,name='Scrypt',active=True,description='Scrypt',slug='scrypt')
    scrypt.save()

def load_currencies(apps, schema_editor):
    Currency = apps.get_model("coins", "Currency")
    dotcoin = Currency(id=1,name='Dotcoin',symbol='DOT',alt_symbol='',active=True,slug='dotcoin')
    dotcoin.save()


def load_coins(apps, schema_editor):
    Coin = apps.get_model("coins", "Coin")
    bitcoin = Coin(id=1,name='Bitcoin',symbol='BTC',alt_symbol='XBT',code='',logo='',pair='0,128',algorithm_id=1,active=True,slug='bitcoin')
    bitcoin.save()
    litecoin = Coin(id=2,name='Litecoin',symbol='LTC',alt_symbol='',code='',logo='',pair='48,176',algorithm_id=2,active=True,slug='litecoin')
    litecoin.save()

def load_exchanges(apps, schema_editor):
    Exchange = apps.get_model("coins", "Exchange")
    cryptopia = Exchange(id=1,name='Cryptopia',apihostname='https://www.cryptopia.co.nz',apimarketsapi='',apimarketmapname='',apimarketmapid='',apicurrencyapi='api',apiresults='Data',apimapname='',apimapsymbol='',apimapalgo='',url='',afflink='',active=True,slug='cryptopia')
    cryptopia.save()

def load_markets(apps, schema_editor):
    Market = apps.get_model("coins", "Market")
    cryptopia = Market(id=1,name='BTC / DOT', marketcode='',marketcode2='',exchangecoincode='',exchangecoincode2='',exchangecurrencycode='',exchangecurrencycode2='',volume_coin=0,volume_currency=0,price_low=0,price_high=0,active=True,coinid_id=1,currencyid_id=1,exchangeid_id=1,slug='btc-dot')
    cryptopia.save()

def load_minertypes(apps, schema_editor):
    MinerType = apps.get_model("coins", "MinerType")
    thesminertype = Miner(id=1,name='Minera', description='description',slug='minera')
    thesminertype.save()

def load_miners(apps, schema_editor):
    Miner = apps.get_model("coins", "Miner")
    thesminer = Miner(id=1,name='Test Miner', minertype=1,host='localhost',port=8000,apiurl='/',apiuser='user',apipass='password',active=True,slug='test-miner')
    thesminer.save()

def load_miningpooltypes(apps, schema_editor):
    MiningPoolType = apps.get_model("coins", "MiningPoolType")
    thesminingpooltype = MiningPoolType(id=1,name='NOMP', description='description',slug='nomp')
    thesminingpooltype.save()

def load_miningpools(apps, schema_editor):
    MiningPool = apps.get_model("coins", "MiningPool")
    thesminingpool = MiningPool(id=1,name='Test Pool', description='description',host='localhost',address=None,port=1234,apiurl='/',apikey='/',pooltype=1,active=True,lug='test-pool')
    thesminingpool.save()

class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_algorithms),
        migrations.RunPython(load_currencies),
        migrations.RunPython(load_coins),
        migrations.RunPython(load_exchanges),
        migrations.RunPython(load_markets),
        migrations.RunPython(load_miners),
        migrations.RunPython(load_minertypes),
        migrations.RunPython(load_miningpools),
        migrations.RunPython(load_miningpooltypes),
    ]
