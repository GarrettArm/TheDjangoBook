from django.urls import path
from . import views


app_name = 'contact'
urlpatterns = [
    path('thanks', views.ThanksView.as_view(), name='thanks'),
    path('', views.ContactView.as_view(), name='contact'),

]
