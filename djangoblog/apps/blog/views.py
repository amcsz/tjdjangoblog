from django.shortcuts import render, redirect
from ..oauth.decorators import login_required
from .models import BlogPost
from .forms import CreateForm

# Create your views here.
def index_view(request):
    context = {
        "is_authenticated": request.user.is_authenticated,
        "posts": list(BlogPost.objects.values('title', 'content')),
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
            newpost = BlogPost(title=title, content=content)
            newpost.save()
            return redirect("blog:index")
    else:
        form = CreateForm
    return render(request, "create.html", {"form" : CreateForm})