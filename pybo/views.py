from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("djWJrn~")


def say_hello(request):
    return HttpResponse("hihi")