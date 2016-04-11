from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/index.html$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^login/$', views.login, name='login'),



]