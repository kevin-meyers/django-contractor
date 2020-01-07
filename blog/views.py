from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from blog.models import Blog
from blog.forms import BlogForm

class BlogListView(ListView):
    model = Blog

    def get(self, request):
        blogs = self.get_queryset().all()
        context = {'blogs': blogs}
        return render(request, 'blog/list.html', context)


class BlogDetailView(DetailView):
    model = Blog

    def get(self, request, slug):
        context = {'blog': self.get_queryset().get(slug__iexact=slug)}
        return render(request, 'blog/detail.html', context)


def createBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('blog')

    else:
        form = BlogForm()
        context = {'form': form}
        return render(request, 'blog/create.html', context)
