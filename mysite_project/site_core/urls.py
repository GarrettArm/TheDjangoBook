from django.urls import path, include
from django.contrib import admin
from django.conf import settings

from . import views


urlpatterns = [
    path("admin/", admin.site.urls, name="admin_pnl"),
    path("accounts/signup/", views.SignUpView.as_view(), name="signup"),
    path("accounts/login/", views.MyLoginView.as_view(), name="login"),
    path("accounts/logout/", views.MyLogoutView.as_view(), name="logout"),
    path("current_date_now/", views.CurrentDateView.as_view(), name="current_date"),
    path("contact/", include("contact.urls"), name="contact"),
    path("etextbook/", include("etextbook.urls"), name="etextbook"),
    path("polls/", include("polls.urls"), name="polls"),
    path("ajax_polls/", include("ajax_polls.urls"), name="ajax_polls"),
    path("notegrid/", include("notegrid.urls"), name="notegrid"),
    path("rest_milage/", include("milage.urls"), name="milage"),
    path("api_auth/", include("rest_framework.urls"), name="api_auth"),
    path("shwag_swap/", include("shwagswap.urls"), name="shwag_swap"),
    path("blog/", include("blog.urls"), name="blog"),
    path("", views.FrontView.as_view(), name="frontpage"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__", include(debug_toolbar.urls))] + urlpatterns
