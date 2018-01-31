"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf import settings
# from django.conf.urls import url, include
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
import debug_toolbar

from . import views


urlpatterns = [
    path('current_date_now/', views.current_date),
    path('current_datetime/plus/<int:hours>', views.hours_ahead),
    path('contact/', views.contact),
    path('contact/thanks/', views.thanks_logic),
    path('add/<int:year>/<int:month>/<int:day>/', views.add_nonsense),
    path('add/<int:year>', views.add_nonsense),
    path('books/', include('books.urls'),),
    path('etextbook/', include('etextbook.urls'), name='etextbook'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('chat/', include('chatroom.urls')),
    path('accounts/login/', login),
    path('accounts/logout/', logout),
    path('', views.FrontView.as_view(), name='hello_url'),

]

urlpatterns = [path('__debug__', include(debug_toolbar.urls)), ] + urlpatterns
