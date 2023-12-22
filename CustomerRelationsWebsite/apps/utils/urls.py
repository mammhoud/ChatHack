from django.urls import path
from . import views

urlpatterns = [
    path("", views.starter, name="index"),
    path("demo/", views.demo, name="demo"),
]
