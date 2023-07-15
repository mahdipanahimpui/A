# home views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def say_hello(request): 
    person = {"name": "mahdi"}
    return render(request, 'hello.html', context=person)


def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', context={'todos': all})