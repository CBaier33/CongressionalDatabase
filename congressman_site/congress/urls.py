from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<state_name>", views.state, name="state"),
    path("<state_name>/Senate", views.senate, name="senate"),
    path("<state_name>/House", views.house, name="house")
]
