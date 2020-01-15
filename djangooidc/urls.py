# coding: utf-8

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login', views.openid, name='openid'),
    re_path('^openid/(?P<op_name>.+)$', views.openid, name='openid_with_op_name'),
    re_path('^callback/login/?$', views.authz_cb, name='openid_login_cb'),
    re_path('^logout$', views.logout, name='logout'),
    re_path('^callback/logout/?$', views.logout_cb, name='openid_logout_cb'),
]
