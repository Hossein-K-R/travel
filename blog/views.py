from django.shortcuts import render, get_list_or_404,get_object_or_404
from blog.models import post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def blog_view(request,**kwargs):

    posts = post.objects.filter(status=1)
    if kwargs.get('cat_name') !=  None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') !=  None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') !=  None:
        posts = posts.filter(tags__name__in =[kwargs['tag_name']])

    posts = Paginator(posts,2)
    try:
        pagenumber = request.GET.get('page')
        posts = posts.get_page(pagenumber)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request,pid):
    posts = post.objects.filter(status=1)
    posts = get_object_or_404(posts, pk=pid)
    context = {'posts': posts}
    return render(request, 'blog/blog-single.html', context)


def test(request):
    return render(request, 'test.html')

def blog_search(request):
    posts = post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blogsingle(request):
    return render(request, 'blog/blogsingle.html')
