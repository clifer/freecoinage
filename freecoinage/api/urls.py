from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url(
        regex=r'^markets/$',
        'market_list',,
        name='market_list'
    ),
    url(
        regex=r'^markets/(?P<slug>[\w|\W]+)$',
        'market_detail',,
        name='market_detail'
    ),
)


