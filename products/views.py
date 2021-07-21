from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to return the products page and implement pagination """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search query!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    # Pagination
    paginate = Paginator(products, 8)
    page = request.GET.get('page')
    items = paginate.get_page(page)

    context = {
        'products': products,
        'items': items,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to return product detail """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
