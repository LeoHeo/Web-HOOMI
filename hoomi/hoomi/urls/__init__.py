"""hoomi URL Configuration


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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.http.response import HttpResponse
from django.shortcuts import render
from jobs.views import *


urlpatterns = [
    url(r'^', include("users.urls", namespace='users')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('social.apps.django_app.urls', namespace='social')),

    url(r'^', include("users.urls", namespace='usrers')),
    url(r'^$', History.as_view(), name="history"),
    url(r'^', include("jobs.urls", namespace='jobs')),

    url(r'^api/', include('api.urls', namespace="api")),
    url(r'^api-docs/', include('rest_framework_swagger.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
