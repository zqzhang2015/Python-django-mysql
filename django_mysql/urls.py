"""django_mysql URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include

urlpatterns = [
    # path('admin/', admin.site.urls),

    # url(r'^index', views.index),

    url(r'^mysql/', include('mysqltest.url')),
    url(r'^oracle/', include('oracletest.url'))  # 将以oracle开头的请求缓存起来, 并传递给将要创建的oracletest/url.py中
]
