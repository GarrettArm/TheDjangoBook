from django.urls import path
from etextbook import views

app_name = "etextbook"
urlpatterns = [path("", views.SpreadsheetView.as_view(), name="upload")]
