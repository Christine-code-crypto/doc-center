from django.urls import path

from . import views

app_name ="services"

urlpatterns = [
    path("", views.index, name="index"),
    path("new-request", views.newRequest, name="new-request")
]