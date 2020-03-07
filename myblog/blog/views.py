from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from .models import Blog, Blogtype   # 从同文件夹中model.py引入Blog类
from django.core.paginator import Paginator   # 引进分页器类

from django.conf import settings

# 前端显示的内容

def blog_list(request):   # 显示博客列表
	
	blogs_all_list = Blog.objects.all()
	paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOG_NUMS)  # 每6页进行分页
	page_num = request.GET.get('page', 1)   # 获取页面参数（GET请求）
	page_of_blogs = paginator.get_page(page_num)     # 获取页面
	current_page_num = page_of_blogs.number    # 获取当前页
	# 获取前后5页
	#page_range = [current_page_num - 2, current_page_num - 1, current_page_num, current_page_num + 1, current_page_num + 2]
	# 处理第一页和最后一页的问题，第一页-2和1比较取1，最后一页+2和最后一页比较取小
	page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
	list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))

	# 加上省略页码标记
	if page_range[0] - 1 >= 2:
		page_range.insert(0, '...')
	if paginator.num_pages - page_range[-1] >= 2:
		page_range.append('...')
	# 加上首页和尾页
	if page_range[0] != 1:   # 如果不是首页，插入首页
		page_range.insert(0, 1)
	if page_range[-1] != paginator.num_pages:   # 如果不是尾页，插入尾页
		page_range.append(paginator.num_pages)

	context = {}   # 字典类型
	# context['blogs'] = Blog.objects.all()   # 获取全部博客
	context['blogs'] = page_of_blogs.object_list
	context['page_of_blogs'] = page_of_blogs
	context['page_range'] = page_range
	context['blogs_count'] = Blog.objects.all().count()   # 显示博客数量
	context['blog_types'] = Blogtype.objects.all()
	return render_to_response('blog_list.html', context)


def blog_detail(request, blog_pk):   # 显示文章具体内容
	context = {}    # 字典类型
	context['blog'] = get_object_or_404(Blog, pk=blog_pk)
	return render_to_response('blog_detail.html', context)


def blogs_with_type(request, blog_type_pk):    # 显示类型总文章
	context = {}
	blog_type = get_object_or_404(Blogtype, pk=blog_type_pk)
	context['blog_type'] = blog_type
	context['blogs'] = Blog.objects.filter(blog_type=blog_type)
	context['blog_types'] = Blogtype.objects.all()
	return render_to_response('blogs_with_type.html', context)
