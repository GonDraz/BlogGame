from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def base(request):
    return home(request)

def home(request):
    return render(request, 'base/home.html')

def contact(request):
    return render(request, 'base/contact.html')