from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='login_app/home.html'), name='home'),
    url(r'^login_app/', include('login_app.urls')),
    url(r'^admin/', admin.site.urls),
]
