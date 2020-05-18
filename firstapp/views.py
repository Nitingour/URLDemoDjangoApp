from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def f1(request):
    return HttpResponse("<h1>From firstapp f1</h1>")


def f2(request):
    return HttpResponse("<h1>From firstapp f2</h1>")
