from django.urls import path
from etextbook import views

app_name = 'etextbook'
urlpatterns = [
    path('bookstore-spreadsheet/', views.read_spreadsheet, name='upload_spreadsheet'),
    path('', views.read_spreadsheet),
]
