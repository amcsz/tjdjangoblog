from celery import shared_task
from .models import Comment, BlogPost

@shared_task
def update_times():
    for obj in BlogPost.objects.all():
        obj.update_time_diff()