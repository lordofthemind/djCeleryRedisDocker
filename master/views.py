from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .tasks import add


def masterindex(request):

    add.delay(3, 7)

    return HttpResponse('Hello, index page for app master from django celery redis docker is ready.')
