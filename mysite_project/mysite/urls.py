from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
import debug_toolbar

from . import views


urlpatterns = [
    path('current_date_now/', views.current_date),
    path('current_datetime/plus/<int:hours>', views.hours_ahead),
    path('add/<int:year>/<int:month>/<int:day>/', views.add_nonsense),
    path('add/<int:year>', views.add_nonsense),
    path('books/', include('books.urls'),),
    path('contact/', include('contact.urls'), name='contact'),
    path('etextbook/', include('etextbook.urls'), name='etextbook'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('chat/', include('chatroom.urls')),
    path('accounts/login/', login),
    path('accounts/logout/', logout),
    path('', views.FrontView.as_view(), name='hello_url'),

]

urlpatterns = [path('__debug__', include(debug_toolbar.urls)), ] + urlpatterns
