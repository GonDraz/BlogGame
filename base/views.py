from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


pages = 'pages/'


def import_view(app="", view=""):
    return pages + app + view + '.html'


def base(request):
    return home(request)


def home(request):
    return render(request, import_view(view='home'))


def contact(request):
    return render(request, import_view(view='contact'))


def handler500(request):
    return render(request, import_view(view='error'))


def handler404(request, exception):
    return render(request, import_view(view='error'), {'exception': exception, })
