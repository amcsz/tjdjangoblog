from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from ..oauth.decorators import login_required
from .models import BlogPost, PostComment, Comment
from .forms import CreateForm, CommentForm

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
        form = CreateForm(request.POST)
        if (form.is_valid()):
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            op = str(request.user.username)
            newpost = BlogPost(title=title, content=content, op=op)
            newpost.save()
            return redirect("blog:index")
    else:
        form = CreateForm
    return render(request, "create.html", {"form" : CreateForm})

def post_view(request, id=-1):
    context = {}
    post = get_object_or_404(BlogPost, pk=id)
    if id != -1:
        context['error'] = False;
        context['post'] = post
        context['form'] = CommentForm
        context['post_id'] = id
        context['comments'] = PostComment.objects.filter(blogpost=post).select_related('comment').order_by('-comment__created_at')
    else:
        context['error'] = True
    if (context['error'] == True): return redirect("blog:index")
    return render(request, "post.html", context=context)

def comment_view(request, id=-1):
    if request.method == 'POST' and id != -1:
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            parentpost = BlogPost.objects.get(pk=id)
            newcomment = Comment(content=content, poster=request.user.username)
            newcomment.save()
            addcomment = PostComment(
                comment = newcomment,
                blogpost = parentpost
            )
            addcomment.save()
            print(addcomment)
    return redirect(reverse('blog:post', kwargs={'id': id}))