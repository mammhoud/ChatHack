from django.urls import path
from . import views

urlpatterns = [
    path("", views.starter, name="index"),
    path("starter/", views.starter, name="starter"),
]
