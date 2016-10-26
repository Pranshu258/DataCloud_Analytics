from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def api(request):
    if request.user.is_authenticated:
        rclient = request.GET.get('client')
        rparam = request.GET.get('params')
        return HttpResponse(models.Activity.objects.filter(client=rclient).values_list(rparam, flat=True))
    else:
        return HttpResponse("you are not logged in")

def collect(request):
    # add assymetric key encryption here to protect the data that was sent
    
    # Following parameters are recieved via the get request
    rclient = request.GET.get("client")
    ractivity = request.GET.get("activity")
    ractivity_type = request.GET.get("activity_type")
    ruser = request.GET.get("user")
    rage = request.GET.get("age")
    rgender = request.GET.get("gender")
    rlocation = request.GET.get("location")
    # http://127.0.0.1:8000/services/collect?client=netflix&activity=thekilling&activity_type=thriller&user=pikachu&age=21&gender=M&location=india

    # Validate the data recieved
    validated = False
    if rclient and ractivity and ractivity_type and ruser and rage and rgender and rlocation:
        validated = True

    # Create an entry in the activity table
    if validated:
        activity = models.Activity(
            client = rclient,
            activity = ractivity,
            activity_type = ractivity_type,
            user = ruser,
            age = rage,
            gender = rgender,
            location = rlocation
        )
        activity.save()

    return HttpResponse("recieved")

