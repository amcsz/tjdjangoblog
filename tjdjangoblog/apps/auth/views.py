from django.shortcuts import render
from ..blog.views import index_view as blog_index_view

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return blog_index_view(request)
    return render(request, 'auth/login.html')
