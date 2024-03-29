# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

def load_users(apps, schema_editor):
    User = apps.get_model("users", "User")
    user = User(id=2,password='pbkdf2_sha256$24000$HbQxNf5RVlH7$wouOZFjzv/0AenphG2C7ort6ufzo5VStbbe1Va0w3XQ=',last_login='1970-01-01',is_superuser=False,username='demo', first_name='demo',last_name='user',email='none@none.com',is_staff=False,is_active=True,date_joined='1970-01-01',name='demo')
    user.save()

#    EmailConfirm = apps.get_model('account', 'emailaddress').objects.get(email=user.email)
#    emailconfirm.verified=True
#    emailconfirm.primary=True
#    emailconfirm.save()

def load_usercoins(apps, schema_editor):
    UserCoin = apps.get_model("users", "UserCoin")
    User = apps.get_model('users', 'User').objects.get(pk=2)
    Coin = apps.get_model('coins', 'Coin').objects.get(pk=1)
    coin = UserCoin(id=1,user=User,coin=Coin,active=True)
    coin.save()

def load_userminers(apps, schema_editor):
    UserMiner = apps.get_model("users", "UserMiner")
    User = apps.get_model('users', 'User').objects.get(pk=2)
    MinerType = apps.get_model('coins', 'MinerType').objects.get(pk=1)
    thesminer = UserMiner(id=1,name='Test Miner', user=User,minertype=MinerType,host='localhost',port=8000,apiurl='/',apiuser='user',apipass='password',active=True,slug='test-miner')
    thesminer.save()

def load_userminingpools(apps, schema_editor):
    UserMiningPool = apps.get_model("users", "UserMiningPool")
    User = apps.get_model('users', 'User').objects.get(pk=2)
    PoolType = apps.get_model('coins', 'MiningPoolType').objects.get(pk=1)
    thesminingpool = UserMiningPool(id=1,name='Test Pool', user=User,description='description',host='localhost',address=None,port=1234,apiurl='/',apikey='/',pooltype=PoolType,active=True,slug='test-pool')
    thesminingpool.save()

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('coins', '0002_load_coindata'),
    ]

    operations = [
        migrations.RunPython(load_users),
        migrations.RunPython(load_usercoins),
        migrations.RunPython(load_userminers),
        migrations.RunPython(load_userminingpools),
    ]
