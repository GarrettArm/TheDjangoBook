from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf import settings

from . import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin_pnl'),
    path('accounts/login/', login),
    path('accounts/logout/', logout, {'next_page': '/'}),
    path('current_date_now/', views.CurrentDateView.as_view(), name='current_date'),
    path('contact/', include('contact.urls'), name='contact'),
    path('etextbook/', include('etextbook.urls'), name='etextbook'),
    path('polls/', include('polls.urls'), name='polls'),
    path('ajax_polls/', include('ajax_polls.urls'), name='ajax_polls'),
    path('notegrid/', include('notegrid.urls'), name='notegrid'),
    path('simple_vue/', include('simple_vue.urls'), name='simple_vue'),
    path('vue_drf/', include('vue_test.urls'), name='vue_test'),
    path('api_auth/', include('rest_framework.urls'), name='api_auth'),
    path('', views.FrontView.as_view(), name='frontpage'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls)),
    ] + urlpatterns
