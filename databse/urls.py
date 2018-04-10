from django.urls import path
from . import views
from django.urls import path, include
from django.conf.urls import *


urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
]
