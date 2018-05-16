from django.urls import path, include
from .routers import router
from . import views


app_name = 'vue_test'
urlpatterns = [
    path('api/', include(router.urls), name='api_router'),
    path('class-based/', views.ClassBasedView.as_view(), name='class_based_drf'),
    path('class-based-detail/<int:pk>', views.ClassBasedDetailView.as_view(), name='class_detail'),
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>', views.UserDetail.as_view()),
    path('', views.TestView.as_view(), name='index'),
]
