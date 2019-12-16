from django.shortcuts import render


def Home(request):
    return render(request, 'web/index.html', {})

def About(request):
    return render(request, 'web/about.html', {})
