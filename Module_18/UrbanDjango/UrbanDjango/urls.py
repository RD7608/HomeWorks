"""
URL configuration for UrbanDjango project.

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
from django.urls import path, include
from task2.views import ClassView, func_view
#from task3.views import index, shop, cart
from task4.views import index, shop, cart
from task5.views import sign_up_by_django, sign_up_by_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task2/class_view/',ClassView.as_view(), name='class_view'),
    path('task2/func_view/', func_view, name='func_view'),
#    path('task3/', index),
#    path('task3/shop/', shop),
#    path('task3/cart/', cart),
    path('task4/', index, name='index'),
    path('task4/shop/', shop, name='shop'),
    path('task4/cart/', cart, name='cart'),
    path('task5/', sign_up_by_html, name='html_sign_up'),
    path('task5/django_sign_up/', sign_up_by_django, name='django_sign_up'),
]
