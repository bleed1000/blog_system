from django.shortcuts import render


def index(request):
    context = {
        'title': 'Enter'
    }
    return render(request, '', context)
