from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("<state_name>", views.state, name="state"),
    path("<state_name>/Senate", views.senate, name="senate"),
    path("<state_name>/House", views.house, name="house"),
    path("Senate/<name>", views.senator, name="senator"),
    path("House/<name>", views.representative, name="representative"),

]
