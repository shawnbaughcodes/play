from django.conf.urls import url
from . import views

#  URLS
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^login_user$', views.login),
    url(r'^home$', views.home),
    # url(r'^sports$', views.sport),
    url(r'^sports/add/(?P<id>\d+)$', views.add_sport),
    url(r'^sport/remove/(?P<id>\d+)$', views.remove_sport),
    url(r'^add_event$', views.add_event),
    url(r'^add_team$', views.add_team),
    url(r'^logout$', views.logout)
]
