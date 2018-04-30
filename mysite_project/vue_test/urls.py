from django.urls import path

from . import views


app_name = 'vue_test'
urlpatterns = [
    path('', views.TestView.as_view(), name='index'),
]
