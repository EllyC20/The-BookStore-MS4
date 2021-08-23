from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Avg
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, ProductReview
from .forms import ReviewForm

# Create your views here.


def all_products(request):
    """ A view to return the products page and implement pagination """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search query!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(author__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    # Pagination
    paginate = Paginator(products, 12)
    page = request.GET.get('page')
    items = paginate.get_page(page)

    context = {
        'products': products,
        'items': items,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

"""
def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    review_obj = Review.objects.all()
    current_rating_obj = Review.objects.filter(
        product_id=product_id)
    form = ReviewForm()

    context = {
        'product': product,
        'review_obj' : review_obj,
        'current_rating_obj' : current_rating_obj,
        'form' : form

    }

    return render(request, 'products/product_detail.html', context)
"""


def product_detail(request, product_id):
    """ a view to return product detail """

    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm()

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'products/product_detail.html', context)

"""
def review_form(request):
     A view to return the add review page
    return render(request, 'products/add_review.html')
"""

"""
def add_review(request, product_id):
    Add a review for a product
    product = get_object_or_404(Product, pk=product_id)
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        reviews = product.reviews.all()
        review = form.save(commit=False)
        review.product = product
        review.user = request.user

        if form.is_valid():
            review.save()

            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)
"""


def add_review(request, product_id):
    """
    A view to allow the user to add a review to a product
    """

    product = get_object_or_404(Product, pk=product_id)

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.user = request.user
                review.save()
                messages.success(request, 'Your review was successful')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(
                    request, 'Failed to add your review')
    context = {
        'form': form
    }

    return render(request, context)
