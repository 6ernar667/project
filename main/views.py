from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def mountains(request):
    return render(request, 'main/mountains.html')

def shops(request):
    return render(request, 'main/shops.html')

def shopsportmaster(request):
    return render(request, 'main/shop-sportmaster.html')


