from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse("<h1>Hello, I am your Dashboard !!</h1>")