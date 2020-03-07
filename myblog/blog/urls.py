from django.urls import path
from . import views
# 当前文件夹引入view文件

# 设置路由
urlpatterns = [
    # http://localhost:8000/blog/1
    path('', views.blog_list, name='blog_list'),    # 博客列表
    path('<int:blog_pk>', views.blog_detail, name='blog_detail'),   # 博客具体内容
    path('type/<int:blog_type_pk', views.blogs_with_type, name='blogs_with_type'),    # 博客类型
]