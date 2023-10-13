from django.db.models import Count
from django.utils import timezone

from .models import Post


def unfilter_posts():
    return Post.objects.select_related(
        'location', 'author', 'category'
    ).annotate(
        comment_count=Count('comments')
    ).order_by("-pub_date")


def filter_posts():
    '''Returns filtered post objects.'''
    return unfilter_posts().filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )
