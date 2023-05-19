from django import template
from blog.models import post,category

register = template.Library()


@register.simple_tag(name='post_count')
def posts():
    posts= post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='posts')
def posts():
    posts= post.objects.filter(status=1)
    return posts

@register.inclusion_tag('blog/populerpost.html')
def latestposts():
    posts = post.objects.filter(status=1).order_by('-published_date')
    return {'posts': posts}

@register.inclusion_tag('blog/postcategories.html')
def categories():
    posts = post.objects.filter(status=1)
    categories = category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories': cat_dict}


