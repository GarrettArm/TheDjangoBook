from django.urls import path, include
from .routers import router
from . import views


app_name = "milage"
urlpatterns = [
    path("api/", include(router.urls), name="api_router"),
    path("class-based/", views.ClassBasedView.as_view(), name="class_based_drf"),
    path(
        "class-based-detail/<int:pk>",
        views.ClassBasedDetailView.as_view(),
        name="class_detail",
    ),
    path("", views.BaseView.as_view(), name="index"),
]
