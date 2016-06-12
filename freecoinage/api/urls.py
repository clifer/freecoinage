from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url(
        regex=r'^markets/$',
        view='market_list',
        name='market_list'
    ),
    url(
        regex=r'^markets/(?P<slug>[\w|\W]+)$',
        view='market_detail',
        name='market_detail',
    ),
)


