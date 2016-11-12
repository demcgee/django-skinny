from django.conf.urls import include, url
from . import views

app_name = 'skinnyapp'
urlpatterns = [

    # Create URL for home page
    url(r'^$', views.home, name='home'),

    # Create URL for original URL when short URL is requested
    url(r'^(?P<short_url>\w{6})$', views.redirect, name='redirect'),

    # Create URL for short URL creation
    url(r'^makeshort/$', views.shorten, name='shorten')
]
