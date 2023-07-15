from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request): 
    person = {"name": "mahdi"}
    return render(request, 'hello.html', context=person)


def home(request):
    return render(request, 'home.html')