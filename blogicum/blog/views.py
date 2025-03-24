from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render

from .constants import MAX_POSTS_ON_PAGE
from .models import Category, Location, Post
from .utils import get_filtered_posts

User = get_user_model()


def index(request):
    posts = get_filtered_posts(Post.objects)[:MAX_POSTS_ON_PAGE]
    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request, id):
    post = get_object_or_404(
        get_filtered_posts(Post.objects),
        pk=id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = get_filtered_posts(category.posts.all())
    return render(
        request,
        'blog/category.html',
        {'category': category, 'post_list': posts}
    )


def author_posts(request, username):
    author = get_object_or_404(User, username=username)
    posts = get_filtered_posts(author.posts.all())
    return render(
        request,
        'blog/author.html',
        {'author': author, 'posts': posts}
    )


def location_posts(request, location_id):
    location = get_object_or_404(Location, pk=location_id)
    posts = get_filtered_posts(location.posts.all())
    return render(
        request,
        'blog/location.html',
        {'location': location, 'posts': posts}
    )
