from django.shortcuts import render
from ..oauth.decorators import login_required
from .models import BlogPost

# Create your views here.
def index_view(request):
    context = {
        "is_authenticated": request.user.is_authenticated
    }
    for obj in BlogPost.objects.all():
        print(obj)
    return render(request, "index.html", context)

@login_required
def create_view(request):
    return render(request, "create.html")