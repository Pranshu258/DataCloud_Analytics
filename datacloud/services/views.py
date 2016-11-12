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
        if rparam == 'gender':
            users = set()
            data = [{"gender":"M", "population":0},{"gender":"F", "population":0}]
            for a in array:
                if a.user not in users:
                    gender = a.gender
                    users.add(a.user)
                    print(a.user)
                    if gender == "M":
                        data[0]['population'] += 1
                    else:
                        data[1]['population'] += 1
            print(data)
            return JsonResponse({'response':data})

        # Response if activity stats is asked
        if rparam == 'activity':
            # data = [{"date":"24-Apr-07", "close":95},{"date":"25-Apr-07", "close":65},{"date":"26-Apr-07", "close":155},{"date":"27-Apr-07", "close":165},{"date":"30-Apr-07", "close":265}]
            mont = ['Jan', 'Feb', 'Apr', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Nov', 'Dec']
            resp = {}
            for a in array:
                ts = a.timestamp
                print(ts)
                datestr = str(ts.day) + "-" + mont[ts.month - 1] + "-" + str(ts.year)
                if datestr not in resp:
                    resp[datestr] = 1
                else:
                    resp[datestr] += 1
            
            data = [{"date":"01-Nov-2016", "close":0}]
            for key in resp:
                data.append({"date":key, "close":resp[key]})

            print(data)

            return JsonResponse({'response':data})

        if rparam == 'geoactivity':
            pass

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

