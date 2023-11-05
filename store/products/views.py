from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponseRedirect
from .models import Product, Category, Basket
from users.models import User
from django.db.models import F
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from store.settings import PER_PAGE
from django.views.generic import TemplateView, ListView
from .mixins import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Главная страница'

class ProductsListView(TitleMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 3
    title = 'Каталог'

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        if category_id:
            return queryset.filter(category_id=category_id)
        else:
            return queryset


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

def test(request):
    template = "products/test.html"
    return render(request, template)