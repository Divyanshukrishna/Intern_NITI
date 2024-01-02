from django.contrib import admin
from django.urls import path
from page import views


urlpatterns = [
    path('',views.google, name="google"),
    path('home/',views.home, name="home"),
]