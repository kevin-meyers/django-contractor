from django.forms import ModelForm
from blog.models import Blog


class BlogForm(ModelForm):  # Look into LoginRequiredMixin
    class Meta:
        model = Blog
        fields = ['title', 'content', 'summary', 'image_url']
