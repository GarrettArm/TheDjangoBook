from django.urls import path, include
from django.contrib import admin
from django.conf import settings

from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin_pnl'),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/login/', views.MyLoginView.as_view(), name='login'),
    path('accounts/logout/', views.MyLogoutView.as_view(), name='logout'),
    path('current_date_now/', views.CurrentDateView.as_view(), name='current_date'),
    path('contact/', include('contact.urls'), name='contact'),
    path('etextbook/', include('etextbook.urls'), name='etextbook'),
    path('polls/', include('polls.urls'), name='polls'),
    path('ajax_polls/', include('ajax_polls.urls'), name='ajax_polls'),
    path('notegrid/', include('notegrid.urls'), name='notegrid'),
    path('simple_vue/', include('simple_vue.urls'), name='simple_vue'),
    path('vue_drf/', include('vue_test.urls'), name='vue_test'),
    path('api_auth/', include('rest_framework.urls'), name='api_auth'),
    path('shwag_swap/', include('shwagswap.urls'), name='shwag_swap'),
    # path('chatroom/', include('chatroom.urls')),
    #  view.py would be the normal place for the TemplateView line
    path('react_example', TemplateView.as_view(template_name='react_example/index.html'), name='react_example'),
    path('', views.FrontView.as_view(), name='frontpage'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls)),
    ] + urlpatterns
