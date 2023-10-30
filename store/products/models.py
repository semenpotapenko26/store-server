from django.db import models
from users.models import User
from django.db.models import Count, Sum

class Category(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to="products_images")
    description = models.TextField()
    short_description = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Товар: {self.name} | Категория: {self.category}"


class Basket(models.Model):
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="baskets"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="baskets"
    )

    def __str__(self):
        return f"Корзина для {self.user} | Продукт: {self.product}"
    
    @classmethod
    def sum(cls):
        return cls.quantity * cls.product.price


