from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from . import models
import json

# Create your views here.
def api(request):
    rclient = request.GET.get('client')
    rparam = request.GET.get('params')
    if request.user.is_authenticated and request.user.username == rclient:
        # Create and send a JSON response
        array = models.Activity.objects.filter(client=rclient)
        
        # Response if age demographics were asked
        if rparam == 'age':
            users = set()
            data = [{"age":"<10", "population":0},{"age":"10-20", "population":0},{"age":"20-30", "population":0},{"age":"30-40", "population":0},{"age":"40-50", "population":0},{"age":"50-60", "population":0},{"age":">60", "population":0}]
            for a in array:
                if a.user not in users:
                    age = a.age
                    users.add(a.user)
                    print(a.user)
                    age_range = age % 10
                    if (age_range < 7):
                        data[age_range]['population'] += 1
                    else:
                        data[6]['population'] += 1
            print(data)
            return JsonResponse({'response':data})

        # Response if gender demographics is asked 

        data = serializers.serialize("json", array, fields=(rparam))
        return JsonResponse({'response':data})
    else:
        return HttpResponse("invalid request, either you are not authorized or request was malformed")

def collect(request):
    # add assymetric key encryption here to protect the data that was sent
    ######################################################################

    # Following parameters are recieved via the get request
    rclient = request.GET.get("client")
    ractivity = request.GET.get("activity")
    ractivity_type = request.GET.get("activity_type")
    ruser = request.GET.get("user")
    rage = request.GET.get("age")
    rgender = request.GET.get("gender")
    rlocation = request.GET.get("location")
    # Example Image Request from the Client
    # http://127.0.0.1:8000/services/collect?client=netflix&activity=thekilling&activity_type=thriller&user=pikachu&age=21&gender=M&location=india

    # Validate the data recieved
    validated = False
    if rclient and ractivity and ractivity_type and ruser and rage and rgender and rlocation:
        # Also make sure that the request came from the client only (check the sender)
        ##############################################################################

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

