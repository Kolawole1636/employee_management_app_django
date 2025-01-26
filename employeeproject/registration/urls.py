
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("createuser", views.register, name="register"),

]
