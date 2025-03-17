from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from ..blog.views import index_view

def logout_view(request):
    if request.user.is_authenticated:
        request.user.access_token = None
        request.user.save()
    logout(request)
    return redirect("blog:index")