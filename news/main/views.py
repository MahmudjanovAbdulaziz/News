from django.shortcuts import render
from .models import *


def index(request):
    rows = News.objects.all()
    context = {
        'rows':rows
    }

    return render(request, 'index.html', context)

def singl(request):
    return render(request, 'single.html', {})