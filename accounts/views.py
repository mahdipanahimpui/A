from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def user_register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            # adding first_name and last_name like below, (save it)
            user.first_name = cd['firstname']
            user.last_name = cd['lastname']
            user.save()
            messages.success(request, 'user registered', 'success')
            return redirect('home')

    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', context={'form': form})
    

def user_login(request):

    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                login(request, user)
                messages.success(request, 'user logged in', 'success')
                return redirect('home')
            else:
                messages.warning(request, 'username and password not match')
    else:
        form = UserLoginForm()
    
    return render(request, 'login.html', context={'form': form})




def user_logout(request):
    logout(request)
    messages.success(request, 'user logout', 'success')
    return redirect('home')