from django.shortcuts import render

from .models import *


def index(request):
    context = {
        'segment': 'dashboard',
    }
    return render(request, "dashboard/index.html", context)


def starter(request):
    context = {}
    return render(request, "themes/templates/pages/starter.html", context)



def demo(request):
    context = {}
    return render(request, "themes/templates/pages/demo.html", context)
