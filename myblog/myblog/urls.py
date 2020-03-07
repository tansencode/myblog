"""myblog URL Configuration

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
from django.contrib import admin
from django.urls import include, path  # 设置include路径，包含子类urls路由
from blog.views import blog_list  # blog文件下引入views里的blog_list类
from . import views    # 当前文件夹引入views方法

# 设置总路由
urlpatterns = [
    path('', views.home, name='home'),  # 总路由，首页
    path('admin/', admin.site.urls),   #管理后台路由 
    path('blog/', include('blog.urls')),   # 博客路由

]
