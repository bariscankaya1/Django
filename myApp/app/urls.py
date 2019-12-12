from django.conf.urls import url,include
from django.urls import path
from  app import views
from .views import *
from rest_framework import routers
urlpatterns=[
    url(r'^create/',create),
    url(r'^users/', readJsonFile),
    url(r'^create-api/',createAPI),
]