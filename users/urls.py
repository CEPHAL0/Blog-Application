from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", views.register, name="users-home"),
    path("profile/", views.profile, name="profile"),
]
