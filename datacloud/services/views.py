from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def api(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            rclient = request.GET.get('client')
            rparam = request.GET.get('params')
            return HttpResponse(models.Activity.objects.filter(client=rclient).values_list(rparam, flat=True))
        else:
            return HttpResponse("you are not logged in")
    if request.method == "POST":
        client = request.POST["client"]
        activity = request.POST["activity"]
        activity_type = request.POST["activity_type"]
        user = request.POST["user"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        location = request.POST["location"]
        return HttpResponse(client + " " + location)
