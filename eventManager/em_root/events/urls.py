from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.loginView, name='login'),
    url(r'^logout', views.logoutView, name='logout'),
    url(r'^isLogged/$', views.is_logged_view, name='isLogged'),
    url(r'^addUser/$', views.add_user_view, name='addUser'),
    url(r'^getUser/$', views.get_user_view, name='getUser'),
    url(r'^addEvent/$', views.add_event_view, name='addEvent'),
]
