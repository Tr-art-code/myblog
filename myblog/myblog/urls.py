"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('clock/', views.clock, name='clock'),
    path('main/', views.main, name='main'),
    path('articles/', views.articles, name='articles'),
    path('article/post', views.article_post, name='article_post'),
    path('archive/', views.archive, name='archive'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('test/', views.test, name='test'),
    path('redirection/', views.redirection, name='redirection'),
]
