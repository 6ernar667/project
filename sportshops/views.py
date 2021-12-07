from django.shortcuts import render
from django.http import HttpResponse

def sportshops(request):
    return HttpResponse("<h4>Sportshops!</h4>")
