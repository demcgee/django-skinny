from django.conf.urls import url
from . import views

urlpatterns = [

  #Create URL for home page
  url(r'^$', views.home, name = 'home'),

  #Create URL for original URL when short URL is requested

  #Create URL for short URL creation
]