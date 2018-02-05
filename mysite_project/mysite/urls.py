from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
# import debug_toolbar

from . import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin_pnl'),
    path('accounts/login/', login),
    path('accounts/logout/', logout, {'next_page': '/'}),
    path('current_date_now/', views.current_date, name='current_date'),
    path('books/', include('books.urls'), name='books'),
    path('contact/', include('contact.urls'), name='contact'),
    path('etextbook/', include('etextbook.urls'), name='etextbook'),
    path('polls/', include('polls.urls'), name='polls'),
    path('chat/', include('chatroom.urls'), name='chatroom'),
    path('', views.FrontView.as_view(), name='frontpage'),

]

# urlpatterns = [path('__debug__', include(debug_toolbar.urls)), ] + urlpatterns
