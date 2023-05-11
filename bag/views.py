from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from products.models import Product
from points.models import Points
from django.contrib import messages
from bag.contexts import bag_contents


def view_bag(request):
    ''' View that renders bag content page '''
    user = request.user
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    context = {}
    if request.user.is_authenticated:
        userpoints = Points.objects.filter(user=user)
        user_points = Points.objects.filter(user=user)
        for points in user_points:
            collected_points = int(points.points)
        if collected_points > total:
            context = {'points': points}
            points = True
    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    ''' Add product to the bag '''

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    # Check if the item_id is in the bag
    if item_id not in bag:
        bag[item_id] = {'items_by_size': {}}

    # Check if the items_by_size dictionary exists for the item_id
    if 'items_by_size' not in bag[item_id]:
        bag[item_id]['items_by_size'] = {}

    if size is not None:
        if size in bag[item_id]['items_by_size'].keys():
            bag[item_id]['items_by_size'][size] += quantity
            messages.success(request,
                             (f'Updated size {size.upper()} '
                              f'{product.name} quantity to '
                              f'{bag[item_id]["items_by_size"][size]}'))
        else:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request,
                             (f'Added size {size.upper()} '
                              f'{product.name} to your bag'))
    else:
        if isinstance(bag[item_id], int):
            bag[item_id] += quantity
            messages.success(request,
                             (f'Updated {product.name} '
                              f'quantity to {bag[item_id]}'))
        else:
            if item_id in bag:
                bag[item_id] += quantity
                messages.success(request,
                                 (f'Updated {product.name} '
                                  f'quantity to {bag[item_id]}'))
            else:
                bag[item_id] = quantity
                messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request,
                             (f'Updated size {size.upper()} '
                              f'{product.name} quantity to '
                              f'{bag[item_id]["items_by_size"][size]}'))
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request,
                             (f'Removed size {size.upper()} '
                              f'{product.name} from your bag'))
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request,
                             (f'Updated {product.name} '
                              f'quantity to {bag[item_id]}'))
        else:
            bag.pop(item_id)
            messages.success(request,
                             (f'Removed {product.name} '
                              f'from your bag'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request,
                             (f'Removed size {size.upper()} '
                              f'{product.name} from your bag'))
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)