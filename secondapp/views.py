from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.


def f3(request):
    return HttpResponse("<h1>From secondapp f3</h1>")


def f4(request):
    return HttpResponse("<h1>From secondapp f4</h1>")
