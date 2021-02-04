"""likelion_9th_study3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from showName import views as name
from wordcounter import views as count
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', name.welcome, name="welcome"),
    path('hello/', name.hello, name = "hello"),
    path('wc/', count.home, name = "home"), 
    path('wc/result/', count.result, name = "result"), 
]
