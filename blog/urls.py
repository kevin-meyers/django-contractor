from django.urls import path
from blog.views import BlogListView, BlogDetailView

app_name='blog'
urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('<str:slug>/', BlogDetailView.as_view(), name='detail'),
]
