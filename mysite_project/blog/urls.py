from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('', views.IndexView.as_view(), name='post_list'),
]
