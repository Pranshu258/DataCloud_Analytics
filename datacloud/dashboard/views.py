from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader


def index(request):
    if request.user.is_authenticated:
        return HttpResponse("<h1>Hello, I am your Dashboard !!</h1>")
    else:
        return HttpResponse("<h1>You are not logged in !!!</h1>")