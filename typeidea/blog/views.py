from django.shortcuts import render

# Create your views here.
from blog.models import Tag, Post, Category
from config.models import SideBar


def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:
        tag, p_list = Post.get_by_tag(tag_id)
    elif category_id:
        p_list, category = Post.get_by_category(category_id)
    else:
        p_list = Post.latest_posts()
    context = {
        "category": category,
        "tag": tag,
        "post_list": p_list,
        "sidebars": SideBar.get_all()
    }

    context.update(Category.get_nav())

    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id=None):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    context = {
        'post': post,
        "sidebars": SideBar.get_all(),
    }

    context.update(Category.get_nav())

    return render(request, 'blog/detail.html', context={"post": post})
