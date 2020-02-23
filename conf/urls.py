"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.views.i18n import JavaScriptCatalog
from django.conf.urls import url
# from django.contrib import admin
# from rest_framework import routers
# from common import views as common_views


# router = routers.DefaultRouter()
# router.register(r'users', common_views.UserViewSet)

urlpatterns = [
    # use rest_framework router instead of URL conf
    # path('', include(router.urls)),

    # api authorization
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # shared
    path('favicon.ico', RedirectView.as_view(url=r'static/favicon.ico')),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),

    # app
    path('', include('common.urls')),
    # path('admin/', admin.site.urls),
]
