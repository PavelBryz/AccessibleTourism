from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from .forms import SignUpForm, LoginForm
from django.contrib import messages


def sign_up(request: WSGIRequest):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('signin')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'users_management/signup.html', context=context)


def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users_management/signin.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('suggestions')

        # form is not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        return render(request, 'users_management/signin.html', {'form': form})
