"""
URL configuration for audit_support project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # http://192.168.1.17:8000/ にアクセスしたら一覧へ転送
    path('', RedirectView.as_view(url='/audit/', permanent=True)),
    
    path('admin/', admin.site.urls),
    
    # Django推薦のログイン機能（/accounts/login/ が有効になります）
    path('accounts/', include('django.contrib.auth.urls')),
    
    # アプリ「group_home」の全機能を 'audit/' 以下に配置
    path('audit/', include('group_home.urls')), 
]