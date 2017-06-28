from django.conf.urls import url
from . import views

#  URLS
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^home$', views.home),
    url(r'^sports$', views.sport),
    url(r'^sports/add/(?P<id>\d+)$', views.add_sport),
    url(r'^sport/remove/(?P<id>\d+)$', views.remove_sport),
    url(r'^games/(?P<id>\d+)$', views.sport_event),
    url(r'^games/(?P<id>\d+)/new$', views.new_game),
]
