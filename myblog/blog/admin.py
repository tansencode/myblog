from django.contrib import admin
from .models import Blogtype, Blog   # 从同文件夹中model.py引入Blog，BlogType类


# 注册类
# 即建立管理类和模块数据简单的联系，方便可视化
 # @为修饰符，相当于admin.register(BlogtypeAdmin),修饰类的参数
@admin.register(Blogtype)  
class BlogtypeAdmin(admin.ModelAdmin):
	# 显示博客id和名称，在http://localhost:8000/admin/learning_blog/blogtype/
	list_display = ('id', 'type_name')


# 显示博客各信息，在http://localhost:8000/admin/learning_blog/blog/
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'blog_type', 'author', 'create_time', 'last_update_time')