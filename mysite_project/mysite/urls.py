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
from django.conf.urls import url, include
from django.contrib import admin

from mysite.views import hello
from mysite.views import current_date
from mysite.views import hours_ahead
from mysite.views import contact
from mysite.views import thanks_logic


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^current_date_now/$', current_date),
    url(r'^current_datetime/plus/(\d{1,2})/$', hours_ahead),
    url(r'^contact/$', contact),
    url(r'^contact/thanks/$', thanks_logic),
    url(r'^', include('books.urls')),
]
