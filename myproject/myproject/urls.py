"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm,password_reset_complete
from newsapp.views import *
from django.http import HttpResponse


urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^login/$', display_login, name="display_login"),
    url(r'^register/$', display_register, name = "display_register"),
    url(r'^account_info/', display_account_info, name = "display_account"),
    url(r'^logout_view/$', logout_view, name = "logout_view"),
    url(r'^(?P<article_id>[0-9]+)/$', data, name='data'),
    url(r'^register_account/$', register_account, name = "register_account"),
    url(r'^login_to_account/$', login_to_account, name = "login_to_account"),
    url(r'^get_user_info/(?P<username>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$', get_user_data, name = "get_user_data"),
    url(r'^update_user_data/(?P<username>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$', update_user_info, name = "update_user_info"),
    url(r'^add_comment/$', add_comment, name="add_comment"),
    url(r'^delete_comment/(?P<comment_id>[0-9]+)/$', delete_comment, name = "delete_comment"),
    url(r'^rate/$', rate, name="rate"),
    url(r'^reset_password/$', password_reset, name="reset_password"),
    url(r'^reset_password/done/$', password_reset_done, name="password_reset_done"),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name="password_reset_confirm"),
    url(r'^reset_password/complete/$', password_reset_complete, name="password_reset_complete"),
	url(r'^accounts/login', display_login),
]