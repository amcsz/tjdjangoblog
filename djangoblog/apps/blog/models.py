from django.db import models
from datetime import datetime

# Create your models here.
class Comment(models.Model):
    content = models.TextField(max_length=1000)
    poster = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if (len(self.content) < 10): return self.content
        else: return self.content[:10]


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)
    op = models.CharField(max_length=50)
    comments = models.ManyToManyField(Comment)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    

class PostComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
