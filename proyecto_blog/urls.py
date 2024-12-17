"""
URL configuration for proyecto_blog project.

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
from django.contrib import admin
from django.urls import path
from blog.views import UserListView, UserDetailView, PostListView, PostDetailView, CommentListView, BienvenidoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('indice/', BienvenidoView.as_view(), name='bienvenido'),
    path('usuarios/', UserListView.as_view(), name='usuarios'),
    path('usuarios/<int:pk>/', UserDetailView.as_view(), name='usuario-detalle'),
    path('blog/', PostListView.as_view(), name='entradas'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='entradas-detalle')
]
