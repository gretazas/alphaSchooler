from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page """
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

    return render(request, 'home/index.html', context)
