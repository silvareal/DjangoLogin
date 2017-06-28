from django.conf.urls import url
from . import views as login_app_views
from django.contrib.auth import views as auth_views


app_name = "login_app"

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'login_app/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'login_app/logout.html'}, name='logout'),
]