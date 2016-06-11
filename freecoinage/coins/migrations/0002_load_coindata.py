# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

def load_algorithms(apps, schema_editor):
    Algorithm = apps.get_model("algorithms", "Algorithm")
    sha256 = Algorithm(id=1,name='SHA256',active=True,description='SHA256',slug='sha256')
    sha256.save()
    scrypt = Algorithm(id=2,name='Scrypt',active=True,description='Scrypt',slug='scrypt')
    scrypt.save()

def load_coins(apps, schema_editor):
    Coin = apps.get_model("coins", "Coin")
    bitcoin = Coin(id=1,name='Bitcoin',symbol='BTC',alt_symobol='XBT',code='',logo='',pair='0,128',algorithm_id=1,active=True,slug='bitcoin')
    bitcoin.save()
    litecoin = Coin(id=2,name='Litecoin',symbol='LTC',alt_symobol='',code='',logo='',pair='48,176',algorithm_id=2,active=True,slug='litecoin')
    litecoin.save()

def load_exchanges(apps, schema_editor):
    Exchange = apps.get_model("exchanges", "Exchange")
    cryptopia = Exchange(id=1,name='Cryptopia',apihostname='https://www.cryptopia.co.nz',apimarketsapi='',apimarketmapname='',apimarketmapid='',apicurrencyapi='api',apiresults='Data',apimapname='',apimapsymbol='',apimapalgo='',url='',afflink='',active=True,slug='cryptopia')
    cryptopia.save()

def load_markets(apps, schema_editor):
    Market = apps.get_model("markets", "Market")
    cryptopia = Market(id=1,marketcode='',marketcode2='',exchangecoincode='',exchangecoincode2='',exchangecurrencycode='',exchangecurrencycode2='',volume_coin='',volume_currency='',price_low='',price_high='',active=True,coinid_id=1,currencyid_id=1,exchangeid_id=1,slug='btc-dot')
    cryptopia.save()

class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_algorithms),
        migrations.RunPython(load_coins),
        migrations.RunPython(load_exchanges),
        migrations.RunPython(load_markets),
    ]
