from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ Show all products """
    products = Product.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'current_categories': categories,
        'products': products
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Show individual product """
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/product_detail.html', {'product': product})

