from django.urls import path
from . import views


app_name = 'notegrid'
urlpatterns = [
    path('', views.NoteGridView.as_view(), name='notegrid'),
]
