from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import Post, Category, Location


User = get_user_model()


def index(request):
    posts = Post.objects.select_related('category').filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request, id):
    post = get_object_or_404(
        Post.objects.select_related('category'),
        pk=id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = Post.objects.select_related('category').filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category=category
    ).order_by('-pub_date')
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': posts
    })


def author_posts(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        author=author,
        category__is_published=True
    ).order_by('-pub_date')
    return render(
        request,
        'blog/author.html',
        {'author': author, 'posts': posts}
    )


def location_posts(request, location_id):
    location = get_object_or_404(Location, pk=location_id)
    posts = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        location=location,
        category__is_published=True
    ).order_by('-pub_date')
    return render(
        request,
        'blog/location.html',
        {'location': location, 'posts': posts}
    )
