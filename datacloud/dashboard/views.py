from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout

def index(request):
    if request.user.is_authenticated:
        return HttpResponse("<h1>Hello, I am your Dashboard !!</h1><a href='logout/'>logout</a>")
    else:
        return HttpResponse("<h1>You are not logged in !!!</h1>")

def logout_view(request):
    logout(request)
    return redirect('/')