from django.shortcuts import render
from django.http import HttpResponse

def mountains(request):
    return HttpResponse("<h4>Mountains!</h4>")
