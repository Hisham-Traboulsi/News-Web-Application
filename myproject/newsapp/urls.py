from django.conf.urls import url
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm,password_reset_complete
from . import views

this is the list of usrls ecch do various functions, display data and process data and instructions
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.display_login, name="display_login"),
    url(r'^register/$', views.display_register, name = "display_register"),
    url(r'^account_info/', views.display_account_info, name = "display_account"),
    url(r'^logout_view/$', views.logout_view, name = "logout_view"),
    url(r'^(?P<article_id>[0-9]+)/$', views.data, name='data'),
    url(r'^register_account/$', views.register_account, name = "register_account"),
    url(r'^login_to_account/$', views.login_to_account, name = "login_to_account"),
    url(r'^get_user_info/(?P<username>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$', views.get_user_data, name = "get_user_data"),
    url(r'^update_user_data/(?P<username>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$', views.update_user_info, name = "update_user_info"),
    url(r'^add_comment/$', views.add_comment, name="add_comment"),
    url(r'^delete_comment/(?P<comment_id>[0-9]+)/$', views.delete_comment, name = "delete_comment"),
    url(r'^rate/$', views.rate, name="rate"),
    url(r'^reset_password/$', password_reset, name="reset_password"),
    url(r'^reset_password/done/$', password_reset_done, name="password_reset_done"),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name="password_reset_confirm"),
    url(r'^reset_password/complete/$', password_reset_complete, name="password_reset_complete"),
]
