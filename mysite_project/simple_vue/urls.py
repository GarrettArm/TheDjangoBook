from django.urls import path
from . import views


app_name = 'simple_vue'
urlpatterns = [
    path('', views.SimpleVueView.as_view(), name='simple_vue'),
]
