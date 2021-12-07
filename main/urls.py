from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('mountains', views.mountains),
    path('shops', views.shops),
    path('shop-sportmaster', views.shopsportmaster),
]
