from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create_user/$', views.Create_User, name='create_user'),
    url(r'^login/$', views.Login, name='login'),
    url(r'^logout/$', views.Logout, name='logout'),
    url(r'^home/$', views.Home, name='home'),

    url(r'^post/$', views.Post, name='post'),
    url(r'^messages/$', views.Messages, name='messages'),
]
