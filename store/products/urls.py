from django.urls import path
from .views import IndexView, ProductsListView, test, basket_add, basket_remove

app_name = "products"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("products/", ProductsListView.as_view(), name="products_list"),
    path("category/<int:category_id>/", ProductsListView.as_view(), name="category"),
    path("page/<int:page>/", ProductsListView.as_view(), name="paginator"),
    path("basket/add/<int:product_id>/", basket_add, name="basket_add"),
    path("basket/remove/<int:basket_id>/", basket_remove, name="basket_remove"),
    path("test/", test, name="test"),
]
