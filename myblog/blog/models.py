from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blogtype(models.Model):   # 博客的分类
    type_name = models.CharField(max_length=15)   # 分类名称

    def __str__(self):
    	return self.type_name       # 返回显示文章类型

class Blog(models.Model):     # 博文
    title = models.CharField(max_length=50)  # 设置博客标题
    blog_type = models.ForeignKey(Blogtype, on_delete=models.DO_NOTHING)  
    content = models.TextField()             # 内容
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)   # 作者
    create_time = models.DateTimeField(auto_now_add=True)   # 创建时间
    last_update_time = models.DateTimeField(auto_now=True)  # 更新时间

    def __str__(self):
    	return "<Blog:%s>"%self.title  # 显示博客标题

    class Meta:
        ordering = ['-create_time']   # 文章倒序处理，从新到旧
