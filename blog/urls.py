#!/usr/bin/python
# coding: UTF-8
__author__ = 'noma Hwang'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name = 'post_list'),
]