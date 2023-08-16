from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("submit_request/", views.submit_request, name="submit_request"),
    path("manage_request/", views.manage_request, name="manage_request"),
    path("track_request", views.track_request, name="track_request"),
    path("support", views.support, name= "support")
]
