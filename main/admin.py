from django.contrib import admin

from main.models import Category, Product


@admin.register(Category)
class СategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name', 'description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description',)
