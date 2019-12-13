from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from kit.models import Kit


class KitListView(ListView):

    model = Kit

    def get(self, request):
        context = {'kits': self.get_queryset().all()}
        return render(request, 'kit_list.html', context)


class KitDetailView(DetailView):

    model = Kit

    def get(self, request, slug):
        context = {'kits': self.get_queryset().get(slug__iexact=slug)}
        return render(request, 'kit_page.html', context)
