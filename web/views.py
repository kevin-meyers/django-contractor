from django.shortcuts import render


def Home(request):
    return render(request, 'web/index.html', {})
