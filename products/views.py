from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to return the products page and implement pagination """

    products = Product.objects.all()

    # Pagination
    paginate = Paginator(Product.objects.all(), 8)
    page = request.GET.get('page')
    items = paginate.get_page(page)

    context = {
        'products': products,
        'items': items,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to return product detail """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
