from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.

def index(request, UserName = None):
    UserName = request.GET.get('q')
    if UserName == "toto":
        return JsonResponse({"Type":"Human","Age":21,"IQ":130})
    elif UserName == "nikki":
        return JsonResponse({"Type":"Human(Dumbass)","Age":30 ,"IQ":90})
    else:
        return HttpResponse("Username not found")
    