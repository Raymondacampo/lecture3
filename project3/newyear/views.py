import datetime
from django.shortcuts import render

# Create your views here.
def ny(request):
    x = datetime.datetime.now()
    return render(request, 'newyear/index.html', {
        'newyear': x.month == 1 and x.day == 1
    })