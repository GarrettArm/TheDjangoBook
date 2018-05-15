from django.urls import path, include
from .routers import router
from . import views


app_name = 'vue_test'
urlpatterns = [
    path('api-auth/', include('rest_framework.urls'), name='browsable_rest_api'),
    path('api/', include(router.urls), name='api_router'),
    path('', views.TestView.as_view(), name='index'),
]
