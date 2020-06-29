from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from article.models import Blog, BlogType
from django.core.paginator import Paginator

import markdown
import random
import re


# Create your views here.
def index(request):
    a = get_object_or_404(Blog, title='第一篇test')
    b = Blog.objects.all()
    temp = [b[x].title for x in range(1, len(b))]
    r = random.sample(temp, 2)
    a.content = markdown.markdown(a.content,
                                  extensions=[
                                   'markdown.extensions.extra',
                                  ])
    return render(request, 'index.html', context={'first': a, 'time': a.created_time, 'r1': r[0], 'r2': r[1]})


def article(request, a):
    p = get_object_or_404(Blog, title=a)
    p.content = markdown.markdown(p.content,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'articles.html', context={'data': p})


def all_articles(request):
    t = Blog.objects.all()
    paginator = Paginator(t, 4)
    page_num = request.GET.get('page', 1)
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number
    page_list = [x for x in range(max(current_page_num-2, 1), min(current_page_num+2, paginator.num_pages)+1)]
    if not page_of_blogs.object_list.exists():
        error = '未找到相关文章诶。。。'
        return render(request, 'contents.html', context={'type': error, })
    else:
        data = []
        for i in page_of_blogs.object_list:
            img = '/static/images/welcome.jpg'
            url = re.search(r'\!\[.*\]\((.+)\)', i.content)
            if url is not None:
                img = url.group(1)
            data.append([i.title, img, i.created_time])

        return render(request, 'contents.html', context={'all_data': data, 'type': '全部内容',
                                                         'page_of_blogs': page_of_blogs, 'page_list': page_list,
                                                         })


def categories(request):
    t = BlogType.objects.all()
    types = [t[x].type_name for x in range(len(t))]
    return render(request, 'categories.html', context={'types': types})


def cate_articles(request, types):
    num = get_object_or_404(BlogType, type_name=types)
    t = Blog.objects.filter(blog_type_id=num.id)
    paginator = Paginator(t, 4)
    page_num = request.GET.get('page', 1)
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number
    page_list = [x for x in range(max(current_page_num - 2, 1), min(current_page_num + 2, paginator.num_pages) + 1)]
    if not page_of_blogs.object_list.exists():
        error = '未找到相关文章诶。。。'
        return render(request, 'contents.html', context={'type': error, })
    else:
        data = []
        for i in page_of_blogs.object_list:
            img = '/static/images/welcome.jpg'
            url = re.search(r'\!\[.*\]\((.+)\)', i.content)
            if url is not None:
                img = url.group(1)
            data.append([i.title, img, i.created_time])

        return render(request, 'contents.html', context={'all_data': data, 'type': types,
                                                         'page_of_blogs': page_of_blogs, 'page_list': page_list,
                                                         })


def search_html(request):
    if request.GET.get('content') is not None:
        keywords = request.GET.get('content', '').strip()
        t = Blog.objects.filter(title__icontains=keywords)
        paginator = Paginator(t, 4)
        page_num = request.GET.get('page', 1)
        page_of_blogs = paginator.get_page(page_num)
        current_page_num = page_of_blogs.number
        page_list = [x for x in range(max(current_page_num - 2, 1), min(current_page_num + 2, paginator.num_pages) + 1)]
        if not page_of_blogs.object_list.exists():
            error = '未找到相关文章诶。。。'
            return render(request, 'search_content.html', context={'type': error, })
        else:
            data = []
            for i in page_of_blogs.object_list:
                img = '/static/images/welcome.jpg'
                url = re.search(r'\!\[.*\]\((.+)\)', i.content)
                if url is not None:
                    img = url.group(1)
                data.append([i.title, img, i.created_time])

            return render(request, 'search_content.html', context={'all_data': data, 'type': keywords,
                                                                   'page_of_blogs': page_of_blogs,
                                                                   'page_list': page_list,
                                                                   })
    return render(request, 'search.html')
