from django.conf.urls import url
from etextbook import views


urlpatterns = [
    url(r'bookstore-spreadsheet/$', views.bookstore_spreadsheet, name='bookstore_spreadsheet'),
    url(r'', views.bookstore_spreadsheet),
]
