from django.conf.urls import url
from . import views

#  URLS
urlpatterns = [
    url(r'^$', views.index)
]
