from django.db import models
from humanize import precisedelta
from django.utils.timezone import now


def humanize_time_difference(time):
    diff = now() - time
    seconds = diff.total_seconds()

    if seconds < 60:
        return "less than a minute ago"
    elif seconds < 3600:
        return f"{int(seconds // 60)} minutes ago"
    elif seconds < 86400:
        return f"{int(seconds // 3600)} hours ago"
    elif seconds < 604800:
        return f"{int(seconds // 86400)} days ago"
    else:
        return humanize.naturaltime(diff) + " ago"

# Create your models here.
class Comment(models.Model):
    content = models.TextField(max_length=1000)
    poster = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    time_diff = models.CharField(max_length=1000, default="default time")

    def update_time_diff(self):
        self.time_diff = humanize_time_difference(self.created_at)
        self.save()

    def __str__(self):
        if (len(self.content) < 10):
            return self.content
        else:
            return self.content[:10]


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)
    op = models.CharField(max_length=50)
    comments = models.ManyToManyField(Comment)
    created_at = models.DateTimeField(auto_now_add=True)
    time_diff = models.CharField(max_length=1000, default="default time")

    def update_time_diff(self):
        self.time_diff = humanize_time_difference(self.created_at)
        self.save()

    def __str__(self):
        return self.title
    

class PostComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
