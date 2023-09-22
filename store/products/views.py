from django.shortcuts import render
from .models import Product, Category


def index(request):
    template = 'products/index.html'
    title = "Главная страница"
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'title': title,
        'products': products,
        'categories': categories
    }
    return render(request, template, context)


def products(request):
    template = 'products/products.html'
    title = 'Каталог'
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'title': title,
        'products': products,
        'categories': categories
    }
    return render(request, template, context)