# home views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm, TodoUpdateForm

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

    if request.method == "POST":

        form = TodoCreateForm(request.POST)

        if form.is_valid():
            print('is_valid')
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], body=cd['body'], created=cd['created'])
            messages.success(request, 'Todo create', 'success')
            return redirect('home')

    else:
        # to show form import form class and send as dict
        form = TodoCreateForm()
        
    return render(request, 'create.html', context={'form': form}) 



def update(request, todo_id):

    todo = Todo.objects.get(id=todo_id)

    if request.method == 'POST':
        # if instance not used, update not work, insted create a new object
        form = TodoUpdateForm(request.POST, instance=todo) 
        
        if form.is_valid():
            # clean_data is not required in update
            form.save()
            messages.success(request, 'todo updated', extra_tags='success')
            # detail is url, todo is arg (args is not a str)
            return redirect('detail', todo_id) 
    else:
        form = TodoUpdateForm(instance=todo)
    
    return render(request, 'update.html', context={'form': form})
