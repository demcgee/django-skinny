from django.conf.urls import include, url
from . import views

urlpatterns = [

    # Create URL for home page
    url(r'^$', views.home, name='home'),

    # Create URL for original URL when short URL is requested
    #url(r'^(?P&It;short_id&gt;\w{6})$', 'redirect_original', name='redirectoriginal'),

    # Create URL for short URL creation
    #url(r'^makeshort/$', 'shorten_url', name='shortenurl')
]
