from django.urls import path
from blog.views import BlogListView, BlogDetailView, createBlog

app_name='blog'
urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('create/', createBlog, name='create'),  # Cant find this
    path('<str:slug>/', BlogDetailView.as_view(), name='detail'),
]
