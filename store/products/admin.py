from django.contrib import admin
from .models import Product, Category, Basket


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', 'price', 'quantity',  'image')
    search_fields = ('name', )
    ordering = ('name', )


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp', )
    extra = 1
