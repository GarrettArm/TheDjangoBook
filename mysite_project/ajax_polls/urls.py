from django.urls import path

from . import views


app_name = "ajax_polls"
urlpatterns = [
    path("ajax_polls/", views.AjaxDetails.as_view(), name="ajax_polls"),
    path("", views.IndexView.as_view(), name="index"),
]
