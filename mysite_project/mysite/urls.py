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
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', views.hello, name='hello_url'),
    url(r'^current_date_now/$', views.current_date),
    url(r'^current_datetime/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^contact/$', views.contact),
    url(r'^contact/thanks/$', views.thanks_logic),
    url(r'^review/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/$',
        views.review_details),
    # url('^review/(?P<year>[0-9]{4})', views.review_details),
    url(r'^books', include('books.urls', namespace='books')),
]
