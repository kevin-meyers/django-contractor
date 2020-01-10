from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.utils import timezone


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
        model_instance = form.save(commit=False)
        model_instance.author = request.user
        if form.is_valid():
            print('send help')
            model_instance.timestamp = timezone.now()
            model_instance.save()

            return redirect('/blog/')


    else:
        form = BlogForm()
        context = {'form': form}
        return render(request, 'blog/create.html', context)
