from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^search-form/$', views.search_form, name='search_form_page'),
    url(r'^search/$', views.search),
]
