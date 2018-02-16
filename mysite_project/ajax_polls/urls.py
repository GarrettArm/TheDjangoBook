from django.urls import path

from . import views


app_name = 'ajax_polls'
urlpatterns = [
    path('ajax_polls/', views.AjaxDetails.as_view(), name='ajax_polls'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', views.IndexView.as_view(), name='index'),
]
