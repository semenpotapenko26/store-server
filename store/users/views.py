from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from . forms import UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('products:index'))
    form = UserLoginForm()
    context = {'form': form}
    template = 'users/login.html'
    return render(request, template, context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    form = UserRegistrationForm()
    context = {'form': form}
    template = 'users/registration.html'
    return render(request, template, context)
