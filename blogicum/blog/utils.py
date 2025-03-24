from django.utils import timezone


def get_filtered_posts(queryset):
    return queryset.select_related(
        'author',
        'category',
        'location'
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )
