from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('HOLA')

def greet(request, name):
    return render(request, "hello/index.html", {
        'name': name
    })