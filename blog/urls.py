from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path
from django.contrib import admin
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    path("user/<str:username>", UserPostListView.as_view(), name="blog-post-user"),
    path("about/", views.about, name="blog-about"),
    path("post/<int:pk>", PostDetailView.as_view(), name="blog-post-detail"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="blog-post-update"),
    path("post/create", PostCreateView.as_view(), name="blog-post-create"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="blog-post-delete"),
]
