from django.forms import ModelForm
from .models import Blog


class BlogForm(ModelForm):
    model = Blog
    fields = ['title', 'content', 'summary']
