from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def masterindex(request):
    return HttpResponse('Hello, index page for app master from django celery redis docker is ready.')
