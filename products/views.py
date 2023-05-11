from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """ Show all products """
    products = Product.objects.all()
    categories = None
    sort = None
    direction = None
    query = None

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

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    pencil = ['pencil']
    pencil_softness = products.filter(category__name__in=pencil)
    for item in pencil_softness:
        item.pencil_softness = True
        item.save()
    folders = ['folders']
    folder_sizes = products.filter(category__name__in=folders)
    for item in folder_sizes:
        item.folders = True
        item.save()
    lunch_boxes = ['lunch_boxes']
    lunch_box = products.filter(category__name__in=lunch_boxes)
    for item in lunch_box:
        item.lunch_box = True
        item.save()
    pencil_cases = ['pencil_cases']
    pencil_case = products.filter(category__name__in=pencil_cases)
    for item in pencil_case:
        item.pencil_case = True
        item.save()
    diaries_copies = ['diaries_copies']
    copies = products.filter(category__name__in=diaries_copies)
    for item in copies:
        item.copies = True
        item.save()

    context = {
        'current_categories': categories,
        'current_sorting': current_sorting,
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Show individual product """

    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/product_detail.html', {'product': product})


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product was added successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Product add failed . Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


def mix_match(request):
    products = Product.objects.all()

    categories = None
    query = None
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET.getlist('category')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    quantity = 1
    bags = products.filter(category__name='bags')
    cases = products.filter(category__name='pencil_cases')
    template = 'products/mix_match.html'
    context = {
        'current_categories': categories,
        'products': products,
        'search_term': query,
        'bags': bags,
        'cases': cases,
    }
    return render(request, template, context)