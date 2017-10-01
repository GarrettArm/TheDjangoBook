from django.conf.urls import url
from etextbook import views


urlpatterns = [
    url(r'bookstore-spreadsheet/$', views.read_spreadsheet, name='upload_spreadsheet'),
    url(r'', views.read_spreadsheet),
]
