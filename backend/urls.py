from .models import *
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('article/', views.article, name="article"),
    path('categorie/', views.categorie, name="categorie"),
    path('vente/', views.vente, name="vente"),
    path('stock/', views.stock, name="stock"),

]