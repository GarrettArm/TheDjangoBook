from django.urls import path
from . import views


app_name = "shwag_swap"
urlpatterns = [
    path("", views.ShwagTakeView.as_view(), name="shwag_take"),
    path("deals", views.ShwagDealsView.as_view(), name="shwag_deals"),
    path("email_author", views.EmailAuthorView.as_view(), name="email_author"),
]
