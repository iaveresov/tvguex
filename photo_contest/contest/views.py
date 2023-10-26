from django.shortcuts import render
from django.http import HttpResponse
from .models import MyName


def index(request):

    names = [str(name) for name in MyName.objects.all()]
    return render(
        request,
        'contest/index.html',
        context=
        {'names': names},
    )

def login(request, login, password)