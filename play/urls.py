from django.conf.urls import url
from . import views

#  URLS
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^home$', views.home),
    url(r'^sports$', views.sport),
    url(r'^sports/add/(?P<id>\d+)$', views.add_sport),
]
