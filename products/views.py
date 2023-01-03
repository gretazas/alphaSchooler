from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def all_products(request):
    """ Show all products """
    products = Product.objects.all()
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'current_categories': categories,
        'current_sorting': current_sorting,
        'products': products
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Show individual product """
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/product_detail.html', {'product': product})

