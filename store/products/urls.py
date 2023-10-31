from django.urls import path
from .views import index, products, test, basket_add, basket_remove

app_name = "products"

urlpatterns = [
    path("", index, name="index"),
    path("products/", products, name="products_list"),
    path("category/<int:category_id>/", products, name="category"),
    path("page/<int:page_number>/", products, name="paginator"),
    path("basket/add/<int:product_id>/", basket_add, name="basket_add"),
    path("basket/remove/<int:basket_id>/", basket_remove, name="basket_remove"),
    path("test/", test, name="test"),
]
