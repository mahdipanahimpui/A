from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
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
    

