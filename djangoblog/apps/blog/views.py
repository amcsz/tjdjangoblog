from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from ..oauth.decorators import login_required
from .models import BlogPost, PostComment, Comment
from .forms import BlogPostForm, CommentForm

# Create your views here.
def index_view(request):
    posts = BlogPost.objects.order_by('-created_at').values('title', 'content', 'op', 'id', 'created_at')
    context = {
        "is_authenticated": request.user.is_authenticated,
        "posts": list(posts),
        "user": request.user
    }
    return render(request, "index.html", context)

@login_required
def create_view(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if (form.is_valid()):
            post = form.save(commit=False)
            post.op = request.user.username
            post.save()
            return redirect("blog:index")
    return render(request, "create.html", {"form" : BlogPostForm})

def post_view(request, id):
    post = get_object_or_404(BlogPost, pk=id)
    context = {
        "post": post,
        "form": CommentForm,
        "post_id": id,
        "comments": PostComment.objects.filter(blogpost=post).select_related('comment').order_by('-comment__created_at'),
        "is_authenticated": request.user.is_authenticated,
    }
    return render(request, "post.html", context)

@login_required
def comment_view(request, id):
    post = get_object_or_404(BlogPost, pk=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            newcomment = form.save(commit=False)
            newcomment.poster = request.user.username
            newcomment.save()
            PostComment.objects.create(comment=newcomment, blogpost=post)
    return redirect(reverse('blog:post', kwargs={'id': id}))