from django.contrib import admin
from .models import Product, Category, ProductReview

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'price',
        'category'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductReview)
