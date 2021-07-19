from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to return the products page """

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
