from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic

@login_required
def index_view(request):
    return render(request, "blog/index.html")