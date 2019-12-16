from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from blog.models import Blog


class BlogListView(ListView):
    model = Blog

    def get(self, request):
        blogs = self.get_queryset().all()
        context = {'blogs': blogs}
        return render(request, 'blog/list.html', context)


