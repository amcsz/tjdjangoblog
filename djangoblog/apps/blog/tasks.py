from celery import shared_task
from .models import BlogPost, PostComment
from django.shortcuts import get_object_or_404 # type: ignore

@shared_task
def update_blog_times():
    for obj in BlogPost.objects.all():
        obj.update_time_diff()

@shared_task
def update_time_specific(post_pk):
    BlogPost.objects.get(pk=post_pk).update_time_diff()

@shared_task
def update_comment_times(post_pk):
    post = get_object_or_404(BlogPost, pk=post_pk)
    for comment in PostComment.objects.filter(blogpost=post).select_related('comment'):
        comment.comment.update_time_diff()
