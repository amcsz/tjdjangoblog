from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path('', views.index_view, name="index"),
    path('create/', views.create_view, name="create"),
    path('post/<int:id>/', views.post_view, name="post"),
    path('comment/<int:id>/', views.comment_view, name="comment")
]