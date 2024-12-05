from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.

def index(request):
    query = request.GET.get('q')
    if query == "toto":
        return JsonResponse({"Type":"Human","Age":21,"IQ":130})
    elif query == "nikki":
        return JsonResponse({"Type":"Human(Dumbass)","Age":30 ,"IQ":90})