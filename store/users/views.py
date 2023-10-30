from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

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
    else:
        form = UserLoginForm()
    context = {'form': form}
    template = 'users/login.html'
    return render(request, template, context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('products:index'))


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы зарегистрированы!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    template = 'users/registration.html'
    return render(request, template, context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(
            instance=request.user, data=request.POST, files=request.FILES
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    form = UserProfileForm(instance=request.user)
    total_quantity = Basket.objects.aggregate(
        total_quantity=Sum('quantity')).get('total_quantity')
    total_sum = Basket.objects.filter(
        user=request.user).aggregate(total_sum=Sum('product__price')).get('total_sum')
    print(total_sum)
    title = 'Профиль пользователя'
    template = 'users/profile.html'
    basket = Basket.objects.filter(user=request.user)
    context = {'title': title,
               'form': form,
               'basket': basket,
               'total_quantity': total_quantity,
               'total_sum': total_sum
               }
    return render(request, template, context)
