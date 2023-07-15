# home views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm

# Create your views here.



def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', context={'todos': all})



def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', context={'todo': todo})


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    messages.success(request, 'toto Deleted', extra_tags='success')
    return redirect('home') # home url name


def create(request):
    # to show form import form class and send as dict
    form = TodoCreateForm()
    return render(request, 'create.html', context={'form': form}) 