from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def base(request):
    return home(request)


def home(request):
    return render(request, 'html/pages/home.html')


def contact(request):
    return render(request, 'html/pages/contact.html')


def handler500(request):
    return render(request, 'html/pages/error.html')


def handler404(request, exception):
    return render(request, 'html/pages/error.html', {'exception': exception, })
