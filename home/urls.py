from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^logout$', views.logout_user, name='logout_user'),
    url(r'^login$', views.login_user, name='login_user'),
    url(r'^not_user$', views.notuser, name='notuser'),



]