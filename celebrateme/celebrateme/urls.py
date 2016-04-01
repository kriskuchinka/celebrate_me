"""celebrateme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from celebrateme_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', index, name="index"),
    url(r'^admin/', admin.site.urls),
    url(r'^memorial/(?P<name>[_0-9a-zA-Z]*)$', user_display),
    url(r'^sign_up/create_user$', create_user),
    url(r'^sign_up/$', sign_up),
    url(r'^create_memorial/$', create_memorial),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


