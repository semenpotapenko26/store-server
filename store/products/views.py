from django.shortcuts import render, HttpResponseRedirect
from .models import Product, Category, Basket
from users.models import User
from django.db.models import F
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from store.settings import PER_PAGE

def index(request):
    template = "products/index.html"
    title = "Главная страница"
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {"title": title, "products": products, "categories": categories}
    return render(request, template, context)


def products(request, category_id=None, page_number=1):
    template = "products/products.html"
    title = "Каталог"
    if category_id:
        products = Product.objects.filter(category__id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, PER_PAGE)

    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    context = {
        "title": title,
        "products": page_obj,
        "categories": categories}
    return render(request, template, context)


def test(request):
    template = "products/test.html"
    return render(request, template)

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(product=product, user=request.user)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity = F("quantity") + 1
        basket.save()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
