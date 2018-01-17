from django.conf.urls import include,url
from . import views

urlpatterns = [
        url(r'^$', views.users_list, name='inicio'),        
        url(r'^profe/(?P<pk>[0-9]+)/$', views.perfil_profe, name='perfil_profe'),
        url(r'^alumno/(?P<pk>[0-9]+)/$', views.perfil_alumno, name='perfil_alumno'),
        url(r'^alumno/(?P<pk>[0-9]+)/ayuda/$', views.ayuda, name='ayuda'),
        url(r'^bien/(?P<pk>[0-9]+)$', views.bien, name='bien'),
        url(r'^bien/nuevo/$', views.nuevo_bien, name='nuevo_bien'),
    ]