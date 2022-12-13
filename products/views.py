from django.shortcuts import render
from .models import Product


def all_products(request):
    """ Show all products """
    products = Product.objects.all()

    return render(request, 'products/products.html', {'products': products})

