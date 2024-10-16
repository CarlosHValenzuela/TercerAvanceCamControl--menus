"""
URL configuration for Capstone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='/'),
    path('main', views.main, name='main'),
    path('', views.inicioSesion, name='/'),
    path('cerrarSesion', views.cerrarSesion, name='cerrarSesion'),
    path('registro', views.registro, name='registro'),
    path('reconocedor', views.reconocedor, name='reconocedor'),
    path('captura', views.captura, name='captura'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('video_capture', views.video_capture, name='video_capture'),
    path('residentes', views.residentes, name='residentes'),
    path('perfil', views.perfil, name='perfil'),
]